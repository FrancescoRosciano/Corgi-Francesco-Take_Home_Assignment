#!/usr/bin/env python3
"""
Script to rename folders in the final/ directory with ##_ prefix.
Excludes the 0_pdfs folder from renaming.
"""

import os
import shutil
from pathlib import Path


def rename_folders_with_prefix():
    """Rename folders in final/ directory with ##_ prefix."""
    
    # Define the base directory
    base_dir = Path("/Users/francescorosciano/Desktop/codes/Corgi_Take_Home_Assignment/final")
    
    if not base_dir.exists():
        print(f"Error: Directory {base_dir} does not exist")
        return
    
    # Get all directories in the final folder
    directories = [d for d in base_dir.iterdir() if d.is_dir()]
    
    # Filter out the 0_pdfs directory
    directories_to_rename = [d for d in directories if d.name != "0_pdfs"]
    
    # Sort directories alphabetically for consistent numbering
    directories_to_rename.sort(key=lambda x: x.name)
    
    print(f"Found {len(directories_to_rename)} directories to rename:")
    
    # Rename each directory
    for i, directory in enumerate(directories_to_rename, 1):
        # Create new name with ##_ prefix (using 2-digit zero-padded number)
        new_name = f"{i:02d}_{directory.name}"
        new_path = base_dir / new_name
        
        print(f"Renaming: {directory.name} -> {new_name}")
        
        try:
            # Rename the directory
            directory.rename(new_path)
            print(f"✓ Successfully renamed to {new_name}")
        except Exception as e:
            print(f"✗ Error renaming {directory.name}: {e}")
    
    print(f"\nRenaming complete! {len(directories_to_rename)} directories processed.")


if __name__ == "__main__":
    rename_folders_with_prefix()
