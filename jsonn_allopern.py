
######################################### Python JSON

# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.

########################## Parse JSON - Convert from JSON to Python

# If you have a JSON string, you can parse it by using the json.loads() method.
import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# print(type(x))
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
# print(y["age"])
# print(type(y))


################################ Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# print(type(x))

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
# print(y)
# print(type(y))


#   You can convert Python objects of the following types, into JSON strings:
# dict
# list
# tuple
# string
# int
# float
# True
# False
# None


################## Format the Result
import json

a = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# print(json.dumps(a))
# Use the indent parameter to define the numbers of indents:
# print(json.dumps(a, indent=4))


# You can also define the separators, default value is (", ", ": "),
# which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:
# Use the separators parameter to change the default separator:
# print(json.dumps(a, indent=4, separators=(". ", " = ")))

############################ Order the Result
# The json.dumps() method has parameters to order the keys in the result:
# Use the sort_keys parameter to specify if the result should be sorted or not:
# print(json.dumps(x, indent=4, sort_keys=True))


############################ corrupted records



