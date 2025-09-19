#!/usr/bin/env python3
import os
import sys
import json
import glob
import argparse
from typing import Any, Dict, List, Optional, Tuple

import yaml
import pandas as pd
from tqdm import tqdm
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    from openai import OpenAI
    from openai import BadRequestError  # type: ignore
except Exception:  # pragma: no cover
    OpenAI = None  # type: ignore
    BadRequestError = Exception  # type: ignore


DEFAULT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUTPUT_CSV = os.path.join(DEFAULT_ROOT, "policy_scores.csv")
MODEL = "gpt-5"
OPENAI_BASE_URL = os.environ.get("OPENAI_BASE_URL", None)
SEED = int(os.environ.get("OPENAI_SEED", "12345"))

CATEGORIES = {
    "core": [
        "trigger",
        "defense_costs",
        "consent_settle_hammer",
        "erp_tail",
        "retro_date",
    ],
    "coverage": [
        "tech_prof_services",
        "tech_products",
        "media_ip",
        "privacy_regulatory",
        "business_interruption_dbi",
        "pci_reputational",
    ],
    "defs_carves": [
        "defs_clarity",
        "carvebacks_major_exclusions",
    ],
    "limits": [
        "sublimits_breach_bi_reg_pci",
        "retentions_alignment",
    ],
    "ops": [
        "panel_counsel_flex",
        "notice_practicality_services",
    ],
}

DEFAULT_WEIGHTS = {
    "core": 0.30,
    "coverage": 0.30,
    "defs_carves": 0.20,
    "limits": 0.10,
    "ops": 0.10,
}

WEIGHTS_B2B_SAAS = {
    "core": 0.25,
    "coverage": 0.35,
    "defs_carves": 0.25,
    "limits": 0.10,
    "ops": 0.05,
}

WEIGHTS_CONSUMER = {
    "core": 0.25,
    "coverage": 0.35,
    "defs_carves": 0.20,
    "limits": 0.10,
    "ops": 0.10,
}

BONUS_PENALTY_FLAGS = {
    "defense_inside_limits": {
        "low_limit_penalty": -10,
        "high_limit_penalty": -5,
    },
    "hammer": {
        "hard_100": -10,
        "soft_50": -3,
        "none_or_consent_only": 3,
    },
    "incident_response_panel": 2,
    "dependent_bi": 3,
}


def read_yaml_file(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def find_output_yaml_files(root: str) -> List[str]:
    pattern = os.path.join(root, "policies_details", "all", "**", "output.yaml")
    return sorted(glob.glob(pattern, recursive=True))


def normalize_category(scores: Dict[str, float]) -> float:
    if not scores:
        return 0.0
    num_items = len(scores)
    max_total = 5.0 * num_items
    total = sum(max(0.0, min(5.0, float(v))) for v in scores.values())
    return total / max_total if max_total > 0 else 0.0


def compute_bonus_penalties(bp: Dict[str, Any], per_claim_limit: Optional[float]) -> float:
    total = 0.0
    if bp.get("defense_inside_limits") and per_claim_limit is not None:
        if per_claim_limit <= 2_000_000:
            total += BONUS_PENALTY_FLAGS["defense_inside_limits"]["low_limit_penalty"]
        else:
            total += BONUS_PENALTY_FLAGS["defense_inside_limits"]["high_limit_penalty"]

    hammer = bp.get("hammer")
    if hammer == "hard_100":
        total += BONUS_PENALTY_FLAGS["hammer"]["hard_100"]
    elif hammer == "soft_50":
        total += BONUS_PENALTY_FLAGS["hammer"]["soft_50"]
    elif hammer == "none_or_consent_only":
        total += BONUS_PENALTY_FLAGS["hammer"]["none_or_consent_only"]

    if bp.get("incident_response_panel"):
        total += BONUS_PENALTY_FLAGS["incident_response_panel"]
    if bp.get("dependent_bi_endorsement"):
        total += BONUS_PENALTY_FLAGS["dependent_bi"]
    return total


def aggregate_scores(raw: Dict[str, Any], per_claim_limit: Optional[float]) -> Tuple[float, float, float, float, float, float, float, float, float]:
    core = raw["scores"]["core"]
    coverage = raw["scores"]["coverage"]
    defs_carves = raw["scores"]["defs_carves"]
    limits = raw["scores"]["limits"]
    ops = raw["scores"]["ops"]

    n_core = normalize_category(core)
    n_coverage = normalize_category(coverage)
    n_defs = normalize_category(defs_carves)
    n_limits = normalize_category(limits)
    n_ops = normalize_category(ops)

    bp_total = compute_bonus_penalties(raw.get("bonuses_penalties", {}), per_claim_limit)

    def calc_total(weights: Dict[str, float]) -> float:
        return 100.0 * (
            weights["core"] * n_core
            + weights["coverage"] * n_coverage
            + weights["defs_carves"] * n_defs
            + weights["limits"] * n_limits
            + weights["ops"] * n_ops
        ) + bp_total

    return (
        n_core,
        n_coverage,
        n_defs,
        n_limits,
        n_ops,
        calc_total(DEFAULT_WEIGHTS),
        calc_total(WEIGHTS_B2B_SAAS),
        calc_total(WEIGHTS_CONSUMER),
        bp_total,
    )


def extract_per_claim_limit(policy_yaml: Dict[str, Any]) -> Optional[float]:
    try:
        amount = (
            policy_yaml.get("policy", {})
            .get("limits", {})
            .get("per_claim_limit", {})
            .get("amount")
        )
        return float(amount) if amount is not None else None
    except Exception:
        return None


class DeterministicOpenAI:
    def __init__(self) -> None:
        if OpenAI is None:
            raise RuntimeError("openai package not available")
        self.client = OpenAI(base_url=OPENAI_BASE_URL) if OPENAI_BASE_URL else OpenAI()

    @retry(
        retry=retry_if_exception_type(Exception),
        wait=wait_exponential(multiplier=1, min=1, max=8),
        stop=stop_after_attempt(4),
    )
    def score_policy(self, policy_yaml: Dict[str, Any]) -> Dict[str, Any]:
        instructions = (
            "You are an insurance coverage analyst. Score a single policy across the "
            "specified criteria. Each 0–5 score must be justified with a clause cite. "
            "Citations end with [§ title / p. X]. Keep outputs terse. Return strict JSON only."
        )

        tool_schema = {
            "type": "object",
            "properties": {
                "scores": {
                    "type": "object",
                    "properties": {
                        "core": {
                            "type": "object",
                            "properties": {k: {"type": "number", "minimum": 0, "maximum": 5} for k in CATEGORIES["core"]},
                            "required": CATEGORIES["core"],
                        },
                        "coverage": {
                            "type": "object",
                            "properties": {k: {"type": "number", "minimum": 0, "maximum": 5} for k in CATEGORIES["coverage"]},
                            "required": CATEGORIES["coverage"],
                        },
                        "defs_carves": {
                            "type": "object",
                            "properties": {k: {"type": "number", "minimum": 0, "maximum": 5} for k in CATEGORIES["defs_carves"]},
                            "required": CATEGORIES["defs_carves"],
                        },
                        "limits": {
                            "type": "object",
                            "properties": {k: {"type": "number", "minimum": 0, "maximum": 5} for k in CATEGORIES["limits"]},
                            "required": CATEGORIES["limits"],
                        },
                        "ops": {
                            "type": "object",
                            "properties": {k: {"type": "number", "minimum": 0, "maximum": 5} for k in CATEGORIES["ops"]},
                            "required": CATEGORIES["ops"],
                        },
                    },
                    "required": ["core", "coverage", "defs_carves", "limits", "ops"],
                },
                "cells": {
                    "type": "object",
                    "description": "Short text per matrix cell with clause citation.",
                    "properties": {
                        "what_covered": {"type": "string"},
                        "what_excluded": {"type": "string"},
                        "limits_and_sublimits": {"type": "string"},
                        "notable_definitions_carvebacks": {"type": "string"},
                    },
                    "required": [
                        "what_covered",
                        "what_excluded",
                        "limits_and_sublimits",
                        "notable_definitions_carvebacks",
                    ],
                },
                "bonuses_penalties": {
                    "type": "object",
                    "properties": {
                        "defense_inside_limits": {"type": "boolean"},
                        "policy_limit_millions": {"type": "number"},
                        "hammer": {"type": "string", "enum": ["hard_100", "soft_50", "none_or_consent_only", "other"]},
                        "incident_response_panel": {"type": "boolean"},
                        "dependent_bi_endorsement": {"type": "boolean"},
                    },
                    "required": [
                        "defense_inside_limits",
                        "policy_limit_millions",
                        "hammer",
                        "incident_response_panel",
                        "dependent_bi_endorsement",
                    ],
                },
                "scenarios": {
                    "type": "object",
                    "properties": {
                        "scenario_saas_api_outage_sla": {"type": "number", "minimum": 0, "maximum": 5},
                        "scenario_ugc_defamation_takedown": {"type": "number", "minimum": 0, "maximum": 5},
                        "scenario_rationales": {
                            "type": "object",
                            "properties": {
                                "saas_api_outage_sla": {"type": "string"},
                                "ugc_defamation_takedown": {"type": "string"},
                            },
                            "required": ["saas_api_outage_sla", "ugc_defamation_takedown"],
                        },
                    },
                    "required": [
                        "scenario_saas_api_outage_sla",
                        "scenario_ugc_defamation_takedown",
                        "scenario_rationales",
                    ],
                },
            },
            "required": ["scores", "cells", "bonuses_penalties", "scenarios"],
        }

        messages = [
            {"role": "system", "content": instructions},
            {
                "role": "user",
                "content": (
                    "Score the following policy YAML strictly per schema; provide terse text and "
                    "end each line with a clause citation."
                ),
            },
            {
                "role": "user",
                "content": json.dumps(policy_yaml, ensure_ascii=False),
            },
        ]

        params: Dict[str, Any] = {
            "model": MODEL,
            "messages": messages,
            "seed": SEED,
            "response_format": {"type": "json_schema", "json_schema": {"name": "policy_scoring", "schema": tool_schema}},
        }
        if not MODEL.startswith("gpt-5"):
            params["temperature"] = 0

        try:
            resp = self.client.chat.completions.create(**params)
        except BadRequestError:
            # Fallback: request generic JSON object and parse/validate client-side
            params_fallback = {
                "model": MODEL,
                "messages": messages,
                "seed": SEED,
                "response_format": {"type": "json_object"},
            }
            # keep deterministic if supported
            if not MODEL.startswith("gpt-5"):
                params_fallback["temperature"] = 0
            resp = self.client.chat.completions.create(**params_fallback)

        content = resp.choices[0].message.content or "{}"
        return json.loads(content)


def _process_file(path: str) -> Dict[str, Any]:
    try:
        policy_yaml = read_yaml_file(path)
        policy_name = os.path.basename(os.path.dirname(path))
        per_claim_limit = extract_per_claim_limit(policy_yaml)

        client = DeterministicOpenAI()
        resp = client.score_policy(policy_yaml)

        n_core, n_cov, n_defs, n_lim, n_ops, total_def, total_b2b, total_cons, bp_total = (
            aggregate_scores(resp, per_claim_limit)
        )

        cells = resp.get("cells", {})
        scenarios = resp.get("scenarios", {})

        return {
            "policy": policy_name,
            "file_path": path,
            "n_core": round(n_core, 4),
            "n_coverage": round(n_cov, 4),
            "n_defs_carves": round(n_defs, 4),
            "n_limits": round(n_lim, 4),
            "n_ops": round(n_ops, 4),
            "Score_Default": round(total_def, 2),
            "Score_B2B_SaaS": round(total_b2b, 2),
            "Score_Consumer": round(total_cons, 2),
            "BonusPenalty": round(bp_total, 2),
            "Scenario_SaaS_API": scenarios.get("scenario_saas_api_outage_sla", 0),
            "Scenario_UGC_Defa": scenarios.get("scenario_ugc_defamation_takedown", 0),
            "Cell_WhatCovered": cells.get("what_covered", ""),
            "Cell_WhatExcluded": cells.get("what_excluded", ""),
            "Cell_LimitsSublimits": cells.get("limits_and_sublimits", ""),
            "Cell_NotableDefsCarves": cells.get("notable_definitions_carvebacks", ""),
        }
    except Exception as e:
        return {
            "policy": os.path.basename(os.path.dirname(path)),
            "file_path": path,
            "error": str(e),
        }


def main() -> int:
    parser = argparse.ArgumentParser(description="Score policies from output.yaml files")
    parser.add_argument(
        "--profile",
        choices=["default", "b2b_saas", "consumer"],
        default="default",
        help="Which profile to use for sorting and Top4_Selected",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=11,
        help="Number of parallel workers for OpenAI calls (default: 11)",
    )
    args = parser.parse_args()

    load_dotenv()
    if not os.environ.get("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not set in environment or .env", file=sys.stderr)
        return 1

    files = find_output_yaml_files(DEFAULT_ROOT)
    if not files:
        print("No output.yaml files found under policies_details/all/", file=sys.stderr)
        return 1

    rows: List[Dict[str, Any]] = []
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = {executor.submit(_process_file, path): path for path in files}
        with tqdm(total=len(files), desc="Scoring policies") as pbar:
            for future in as_completed(futures):
                rows.append(future.result())
                pbar.update(1)

    df = pd.DataFrame(rows)
    for col in ["Score_Default", "Score_B2B_SaaS", "Score_Consumer"]:
        if col in df:
            df[f"Rank_{col}"] = df[col].rank(ascending=False, method="min").astype("Int64")
            df[f"Top4_{col}"] = df[f"Rank_{col}"] <= 4

    sort_map = {
        "default": "Score_Default",
        "b2b_saas": "Score_B2B_SaaS",
        "consumer": "Score_Consumer",
    }
    chosen = sort_map[args.profile]
    if chosen in df:
        df.sort_values(by=[chosen], ascending=False, inplace=True, na_position="last")
        df["Top4_Selected"] = df[f"Rank_{chosen}"] <= 4
    else:
        df["Top4_Selected"] = False

    df.to_csv(OUTPUT_CSV, index=False)
    print(f"Wrote {OUTPUT_CSV} with {len(df)} rows (sorted by {chosen if chosen in df else 'none'})")
    return 0


if __name__ == "__main__":
    return_code = main()
    sys.exit(return_code)
