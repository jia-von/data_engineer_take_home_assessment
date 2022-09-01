# Setup:
# Create a virtual environment in order to run the script farm_scripting.py
# farm_api.json was created to replicate an array of JSON objects containing Farm API data.

# Import json module library
import json


# Create a function that accepts arguments, JSON object as strings.
def api_input(json_object_input):

    # Parse JSON string and this will result in Python dictionary data. Refer: https://www.w3schools.com/python/python_json.asp
    api_output = json.loads(json_object_input)

    # Calculate the length of an array to be used with the 'while' loop command below. Dynamically generated values allow functions to be reused. 
    row_number = len(api_output)

    # Use 'while' loop to iterate through the array and checking values in "inventory" that satisfies these conditions. 0 or less: None, 1 or 2: Low, 3 or more: Normal
    i = 0
    while i < row_number:

        # Since 'api_output' is a dictionary, I use the built-in method 'get()' to obtain value from "inventory" key and set the values to 'int' data type.
        # Refer: https://www.w3schools.com/python/python_dictionaries_methods.asp
        x = int(api_output[i].get("inventory"))
        
        # I use 'if statement' to check whether the "inventory" values are 0 or less, 1 or 2, 3 or more.
        # If condition is true, use 'update()' method to insert new key-value pairs and remove specified key, "inventory".
        if x <= 0:
            api_output[i].update({"inventory_level": "None"})
            api_output[i].pop("inventory")
            i += 1
        elif x >= 3:
            api_output[i].update({"inventory_level": "Normal"})
            api_output[i].pop("inventory")
            i += 1
        else: 
            api_output[i].update({"inventory_level": "Low"})
            api_output[i].pop("inventory")
            i += 1
    
    # Convert Python objects into JSON string using 'json.dumps()' method and format the string with idents to produce easy to read format.
    # Refer: https://www.w3schools.com/python/python_json.asp
    print(json.dumps(api_output, indent=4))

# Example 1. The use of 'api_input()' function with the given JSON objects.
# [{"name": "Pig", "inventory": 3}, {"name": "Cow", "inventory": 4}, {"name": "Chicken", "inventory": -1}, {"name": "Dog", "inventory": 1}]
print('Example 1. output:')
api_input('[{"name": "Pig", "inventory": 3}, {"name": "Cow", "inventory": 4}, {"name": "Chicken", "inventory": -1}, {"name": "Dog", "inventory": 1}]')
input('Press Enter to continue...')


# Example 2. The use of 'api_input()' function with two additional objects. 
# [{"name": "Pig", "inventory": 3}, {"name": "Cow", "inventory": 4}, {"name": "Chicken", "inventory": -1}, {"name": "Dog", "inventory": 1}, {"name": "Donkey", "inventory": 6}, {"name": "Cat", "inventory": 4}]
print('Example 2. output:')
api_input('[{"name": "Pig", "inventory": 3}, {"name": "Cow", "inventory": 4}, {"name": "Chicken", "inventory": -1}, {"name": "Dog", "inventory": 1}, {"name": "Donkey", "inventory": 6}, {"name": "Cat", "inventory": 4}]')
input('Press Enter to continue...')

# Example 3. The function below uses JSON object file instead of string.
def api_input_json_file(api_file):

    # Assuming the file is saved in the same directory as farm_function.py script. I open the file using 'open()' function.
    farm_api_file = open(str(api_file), "r")

    # Re-using 'api_input()' function defined previously.
    api_input(farm_api_file.read())
print('Example 3. output:')
api_input_json_file("farm_api.json")
input('Press Enter to end...')