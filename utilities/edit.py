import codecs
import json
import os
from pathlib import Path


def editFile(filepath):
    with codecs.open(filepath, "r", "utf-8-sig") as file:
        print(f"Editing {filepath}")
        data = json.load(file)

    for key in ["MinValue", "MaxValue"]:
        for i, obj in enumerate(data):
            if key in obj:
                if isinstance(obj[key], str) and (
                    obj[key].isdigit() or obj[key].startswith("-")
                ):
                    obj[key] = int(obj[key])
        # sorted_obj = {k: obj[k] for k in sorted(obj)}

        # Update the object in the list with the sorted version
        # data[i] = sorted_obj
    # for obj in data:
    #     if "FieldName" not in obj:
    #         obj["FieldName"] = obj.get("ParamFieldName").split('.')[-1]
    # Check if InputType is "checkbox" and EnumValues does not exist
    # if obj.get("InputType") == "checkbox" and "EnumValues" not in obj:
    #     # Add EnumValues to the object
    #     obj["EnumValues"] = {"True": "True", "False": "False"}

    # Save the modified JSON back to the file with 'utf-8' encoding
    with codecs.open(filepath, "w", "utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4, sort_keys=True)

    print(f"Edited {filepath}")


def editDir(dirpath, filter=".json"):
    for root, dirs, files in os.walk(dirpath):
        for file in files:
            if file.endswith(filter):
                fullpath = Path(root) / file
                editFile(fullpath)


editDir(".", ".config.json")
