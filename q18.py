# 18. Find a package in the Python standard library for dealing with JSON. Import the library module and
# inspect the attributes of the module. Use the help function to learn more about how to use the module.
# Serialize a dictionary mapping 'name' to your name and 'age' to your age, to a JSON string.
# Deserialize the JSON back into Python.

import json

# print(dir(json))
#
# print(help(json))

dict_name = {
    "name": "Shreeti",
    "age": 24
}

#Serialization
json_string = json.dumps(dict_name, indent=4)
print(f'Serialized Dictionary to JSON string : \n {json_string}')

#deserialization
dictionary = json.loads(json_string)
print(f'Deserialized JSON string to Dictionary : \n {dictionary}')

# OUTPUT
#
# Serialized Dictionary to JSON string :
#  {
#     "name": "Shreeti",
#     "age": 24
# }
# Deserialized JSON string to Dictionary :
#  {'name': 'Shreeti', 'age': 24}

