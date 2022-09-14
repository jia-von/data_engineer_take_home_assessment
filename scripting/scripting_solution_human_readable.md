# Background Review
>Use any scripting programming language to solve this problem (eg. JS, Python, etc.). Demonstrate with tests that your solution is correct.
>We are evaluating this from the lens that this is your best possible code.
>Your objective is to transform data coming from the Farm API before loading it into your database
>The data from the Farm API contains 2 fields:
>- name
>- inventory
>Write a **script function** that should receive an array of JSON objects containing Farm API data.
>The function should return an array of JSON with *inventory* values transformed as shown below
and added to a field called *inventory_level*:
>- 0 or less: None
>- 1 or 2: Low
>- 3 or more: Normal
>- `[{name: 'Pig', inventory: 3}, {name: 'Cow', inventory: 4}, {name: 'Chicken', inventory: -1}, {name: 'Dog', inventory: 1}]`
## Analysis
- No clarification what kind of tests to do. No mentioned the ability to use library or not. 
- **Script function** assume to be [python function](https://www.w3schools.com/python/python_functions.asp).
## Setup:
1. Change directory into `scripting` so you can execute `farm_function.py` script function.
2. `farm_api.json` was created to replicate an array of JSON objects containing Farm API data.
3. Example command to execute `farm_function.py` in shell: 
```bash
python farm_function.py
```

## Python script function
Create a function that accepts arguments, JSON object as strings.
```python
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
```

# Example 1. 
The use of `api_input()` function with the given JSON objects.
- JSON objects: `[{"name": "Pig", "inventory": 3}, {"name": "Cow", "inventory": 4}, {"name": "Chicken", "inventory": -1}, {"name": "Dog", "inventory": 1}]`
```python
api_input('[{"name": "Pig", "inventory": 3}, {"name": "Cow", "inventory": 4}, {"name": "Chicken", "inventory": -1}, {"name": "Dog", "inventory": 1}]')
```
Output:
```json
Example 1. output:
[
    {
        "name": "Pig",
        "inventory_level": "Normal"
    },
    {
        "name": "Cow",
        "inventory_level": "Normal"
    },
    {
        "name": "Chicken",
        "inventory_level": "None"
    },
    {
        "name": "Dog",
        "inventory_level": "Low"
    }
]
Press Enter to continue...

```

# Example 2. 
The use of `api_input()` function with two additional objects. 
- JSON objects: `[{"name": "Pig", "inventory": 3}, {"name": "Cow", "inventory": 4}, {"name": "Chicken", "inventory": -1}, {"name": "Dog", "inventory": 1}, {"name": "Donkey", "inventory": 6}, {"name": "Cat", "inventory": 4}]`
```python
api_input('[{"name": "Pig", "inventory": 3}, {"name": "Cow", "inventory": 4}, {"name": "Chicken", "inventory": -1}, {"name": "Dog", "inventory": 1}, {"name": "Donkey", "inventory": 6}, {"name": "Cat", "inventory": 4}]')
```
Output:
```json
Example 2. output:
[
    {
        "name": "Pig",
        "inventory_level": "Normal"
    },
    {
        "name": "Cow",
        "inventory_level": "Normal"
    },
    {
        "name": "Chicken",
        "inventory_level": "None"
    },
    {
        "name": "Dog",
        "inventory_level": "Low"
    },
    {
        "name": "Donkey",
        "inventory_level": "Normal"
    },
    {
        "name": "Cat",
        "inventory_level": "Normal"
    }
]
Press Enter to continue...
```

# Example 3. 
The function below uses JSON object file instead of string.
- File input: `farm_api.json`.
```python
def api_input_json_file(api_file):

    # Assuming the file is saved in the same directory as farm_function.py script. I open the file using 'open()' function.
    farm_api_file = open(str(api_file), "r")

    # Re-using 'api_input()' function defined previously.
    api_input(farm_api_file.read())
```
Example use of `api_input_json_file()`:
```python
api_input_json_file("farm_api.json")
```
Output:
```json
Example 3. output:
[
    {
        "name": "Pig",
        "inventory_level": "Normal"
    },
    {
        "name": "Cow",
        "inventory_level": "Normal"
    },
    {
        "name": "Chicken",
        "inventory_level": "None"
    },
    {
        "name": "Dog",
        "inventory_level": "Low"
    }
]
Press Enter to end...
```