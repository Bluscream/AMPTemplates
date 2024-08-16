import json
import codecs

# Open the JSON file with 'utf-8-sig' encoding to remove BOM if present
with codecs.open('operation-harsh-doorstop-devconfig.json', 'r', 'utf-8-sig') as file:
    data = json.load(file)

# Iterate through each object in the loaded JSON array
for obj in data:
    # Check if InputType is "checkbox" and EnumValues does not exist
    if obj.get("InputType") == "checkbox" and "EnumValues" not in obj:
        # Add EnumValues to the object
        obj["EnumValues"] = {"True": "True", "False": "False"}

# Save the modified JSON back to the file with 'utf-8' encoding
with codecs.open('operation-harsh-doorstop-devconfig.json', 'w', 'utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
