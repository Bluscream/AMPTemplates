import os
from pathlib import Path

mappings = {
    "..metaconfig.json": "-metaconfig.json",
    "..config.json": "-config.json",
    "..ports.json": "-ports.json",
    "..updates.json": "-updates.json",
    "..generator.json": "-generator.json",
    "start.json": "-start.json",
}


def rename_json_files(directory):
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

                with open(file_path, "r") as kvp_file:
                    lines = kvp_file.readlines()

                # Process each line
                for num, line in enumerate(lines, start=1):
                    if any(ext in line for ext in mappings.values()):  # already patched
                        print(f"line {num} in {file} already patched: {line}")
                        continue

                    # Check if the line needs patching
                    # elif any(ext in line for ext in mappings.keys()): # needs patching
                    for suffix in mappings.keys():
                        if suffix in line:  # needs patching
                            print(f"Patching line {num} in {file}: {line}")
                            lines[num - 1] = line.replace(
                                suffix, mappings[suffix]
                            )  # Replace the line with the patched version
                            break  # Break after the first successful patching

                # Write the processed lines back to the file
                with open(file_path, "w") as kvp_file:
                    kvp_file.writelines(lines)


if __name__ == "__main__":
    parent_directory = "."  # Update this path
    rename_json_files(parent_directory)
    # update_kvp_files(parent_directory)
