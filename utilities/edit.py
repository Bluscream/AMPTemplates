import json
import codecs

filepath = 'operation-harsh-doorstop-devconfig.json'

# Open the JSON file with 'utf-8-sig' encoding to remove BOM if present
with codecs.open(filepath, 'r', 'utf-8-sig') as file:
    data = json.load(file)

for i, obj in enumerate(data):
    # Sort the keys of the current object alphabetically
    sorted_obj = {k: obj[k] for k in sorted(obj)}
    
    # Update the object in the list with the sorted version
    data[i] = sorted_obj
# for obj in data:
#     if "FieldName" not in obj:
#         obj["FieldName"] = obj.get("ParamFieldName").split('.')[-1]
    # Check if InputType is "checkbox" and EnumValues does not exist
    # if obj.get("InputType") == "checkbox" and "EnumValues" not in obj:
    #     # Add EnumValues to the object
    #     obj["EnumValues"] = {"True": "True", "False": "False"}

# Save the modified JSON back to the file with 'utf-8' encoding
with codecs.open(filepath, 'w', 'utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
