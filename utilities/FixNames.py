import os
import re
from pathlib import Path

mappings = {
        "metaconfig.json": ".metaconfig.json",
        "config.json": ".config.json",
        "ports.json": ".ports.json",
        "updates.json": ".updates.json",
        "generator.json": ".generator.json"
    }

def rename_json_files(directory):
    # Recursively find all .json files
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                base_name = os.path.basename(file)
                # Check if the file needs renaming
                for old, new in mappings.items():
                    if file.endswith(new):
                        print(f"{base_name} already ends with {new}")
                        break
                    elif file.endswith(old):
                        print(f"{base_name} needs fixing")
                        new_file_path = Path(root) / file.replace(old, new)
                        print(f"Renaming {file} to {new_file_path}")
                        os.rename(Path(root) / file, new_file_path)
                        break

def update_kvp_files(directory):
    # Recursively find all .kvp files
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".kvp"):
                file_path = Path(root) / file
                
                # Open the file and read its content line by line
                with open(file_path, 'r') as kvp_file:
                    for line_number, line in enumerate(kvp_file, start=1):
                        # Check each line against the new suffixes
                        for suffix in mappings.values():
                            if f"{suffix}.json" not in line:
                                continue
                        
                        # If none of the new suffixes are found in the line, it needs to be patched
                        else:
                            # Patch the line here (e.g., insert the new suffix)
                            # This is a placeholder; you'll need to define the exact patching logic
                            print(f"Patching line {line_number} in {file}: New suffix '{suffix}' not found.")
                            # Example patching could involve inserting the new suffix into the

if __name__ == "__main__":
    parent_directory = '.'  # Update this path
    rename_json_files(parent_directory)
    # update_kvp_files(parent_directory)
