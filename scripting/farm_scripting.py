import json

# Create an array of JSON objects containing Farm API data.

farm_api_file = open('farm_api.json', "r")

# Parse the 'farm_api_json' string using json.dumps() to convert into a json object.
api_output = json.loads(farm_api_file.read())

# Write a function that returns an array of JSON with 'inventory' values transformed as shown below and added to a field called 'inventory_level'

# 0 or less: None
# 1 or 2: Low
# 3 or more: Normal

# Expected output {name: 'Pig', inventory_level: 'Normal'}, {name: 'Cow', inventory_level: 'Normal'}, {name: 'Chicken',inventory_level: 'None'}, {name: 'Dog', inventory_level: 'Low'}]

i = 0
while i < 4:
    x = int(api_output[i].get("inventory"))
    if x < 1:
        api_output[i].update({"inventory_level": "None"})
        api_output[i].pop("inventory")
        i += 1
    elif x > 2:
        api_output[i].update({"inventory_level": "Normal"})
        api_output[i].pop("inventory")
        i += 1
    else: 
        api_output[i].update({"inventory_level": "Low"})
        api_output[i].pop("inventory")
        i += 1

print(json.dumps(api_output))