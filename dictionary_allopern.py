## Dictionary

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates keys but allow duplicate values.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
# Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

# 🎯 Why Use Dictionary?
# Dictionaries provide:
# Fast access to values using keys
# Semantic clarity by associating labels (keys) with data (values)
# Efficient data structure for lookups, storage, and organization of data

# Pros of dictionary
# | Advantage           | Explanation                                  |
# | ------------------- | -------------------------------------------- |
# | **Fast lookups**    | Very fast O(1) access time for keys          |
# | **Flexible**        | Stores any type of value                     |
# | **Clear structure** | Easy to understand key-value format          |
# | **Dynamic**         | You can add, update, and delete items easily |

# Cons of dictionary
# | Limitation                           | Explanation                                                      |
# | ------------------------------------ | ---------------------------------------------------------------- |
# | **No ordering** (before Python 3.7)  | Items are unordered (though 3.7+ preserves insertion order)      |
# | **Keys must be unique and hashable** | Can’t use lists or other dictionaries as keys                    |
# | **Slightly more memory usage**       | Compared to list or tuple, more memory is needed for hash tables |
# | **Slower iteration**                 | Compared to lists when order is important                        |

# When to use dictionary
# | Situation                             | Use Dictionary?  |
# | ------------------------------------- | ---------------- |
# | Need to map keys to values            | ✅ Yes            |
# | Need fast lookups by custom labels    | ✅ Yes            |
# | Need ordered data with index access   | ❌ No (use list)  |
# | Need fixed-size and immutable data    | ❌ No (use tuple) |
# | Need only unique values, no key-value | ❌ No (use set)   |



######################################################### 1 Create
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

######################################################### 2 Accessing element
# Dictionary_name[key]
thisdict["brand"]

# There is also a method called get() that will give you the same result:
thisdict.get("brand")

# The keys() method will return a list of all the keys in the dictionary.
thisdict.keys()

# The values() method will return a list of all the values in the dictionary.
thisdict.values()

# The items() method will return each item in a dictionary, as tuples in a list.
thisdict.items()

# for nested dictionary
print(myfamily["child2"]["name"])

######################################################### 2 Add
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)                 # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

# Add using Update()
thisdict.update({"color": "red"})



######################################################### 3 Update

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)             # {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.
thisdict.update({"year": 2020})


######################################################### 4 Delete

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)             # {'brand': 'Ford', 'year': 1964}

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict.popitem()

# The del keyword removes the item with the specified key name:
del thisdict["model"]

# The del keyword can also delete the dictionary completely:
del thisdict

# The clear() method empties the dictionary:
thisdict.clear()


######################################################### 5 Copy

# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1,
# and changes made in dict1 will automatically also be made in dict2.
# There are ways to make a copy, one way is to use the built-in Dictionary method copy().
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

mydict = dict(thisdict)
print(mydict)           # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# A shallow copy creates a new dictionary, but:
# It copies references to the original objects (inner dictionaries, lists, etc.)
# Changes to nested objects affect both original and copied dictionaries
# oth original and shallow share the same list object.

import copy
original = {"name": "Alice", "scores": [90, 80]}
shallow = copy.copy(original)  # or original.copy()

shallow["scores"].append(70)

print(original)  # {'name': 'Alice', 'scores': [90, 80, 70]}
print(shallow)   # {'name': 'Alice', 'scores': [90, 80, 70]}

# A deep copy creates a new dictionary and recursively copies all nested objects.
# Changes to nested objects do not affect the original dictionary.
# deep["scores"] is a completely new list, independent of original["scores"].
import copy

original = {"name": "Alice", "scores": [90, 80]}
deep = copy.deepcopy(original)

deep["scores"].append(70)

print(original)  # {'name': 'Alice', 'scores': [90, 80]}
print(deep)      # {'name': 'Alice', 'scores': [90, 80, 70]}

# | Feature          | Shallow Copy (`dict.copy()` or `copy.copy()`) | Deep Copy (`copy.deepcopy()`) |
# | ---------------- | --------------------------------------------- | ----------------------------- |
# | Top-level object | Copied (new dictionary)                       | Copied (new dictionary)       |
# | Nested objects   | **Referenced (shared)**                       | **Copied (independent)**      |
# | Performance      | Faster (less memory)                          | Slower (more memory)          |
# | Use case         | When nested changes are okay to share         | When full isolation is needed |

original = {"a": [1, 2]}
shallow = copy.copy(original)
deep    = copy.deepcopy(original)

original["a"].append(3)

# Result:
# original -> {'a': [1, 2, 3]}
# shallow  -> {'a': [1, 2, 3]}  (affected)
# deep     -> {'a': [1, 2]}     (not affected)


######################################################### 6 Sort (Farward, Reverse)
# Dictionaries are unordered by nature,
# so you sort keys or items and convert the result into a list of tuples or a new dictionary.

scores = {"Math": 80, "Science": 90, "English": 70}
# Sort by key (Forward)
sorted_by_key = dict(sorted(scores.items()))
# Sort by value (Reverse)
sorted_by_value_desc = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))


######################################################### 7 Looping over it

for x in thisdict:
  print(x)

for x in thisdict:
  print(thisdict[x])

for x in thisdict.values():
  print(x)              # Ford Mustang 1964

for x in thisdict.keys():
  print(x)              # brand model year

for x, y in thisdict.items():
  print(x, y)           # brand Ford model Mustang year 1964

myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
# outer loop run one time then inner loop run n times according to keys
for x, obj in myfamily.items():
    print(x)                    # child1 child2 child3

    for y in obj:
        print(y + ':', obj[y])  # name: Emil year: 2004 name: Tobias year: 2007 name: Linus year: 2011


######################################################### 9 Highest and lowest value

scores = {"Math": 80, "Science": 90, "English": 70}
print("Max:", max(scores.values()))  # 90
print("Min:", min(scores.values()))  # 70


######################################################### 10 Merging two

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

# Method 1 (Python 3.5+)
merged = {**d1, **d2}  # d2 overwrites d1's 'b'

# Method 2 (Python 3.9+)
merged = d1 | d2

######################################################### 11 Convert to other data types

# Convert to list of keys
keys_list = list(scores.keys())

# Convert to list of values
values_list = list(scores.values())

# Convert to list of key-value tuples
items_list = list(scores.items())


######################################################### 12 Searching
# To determine if a specified key is present in a dictionary use the in keyword:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


######################################################### 13 Comparing

d1 = {"a": 1, "b": 2}
d2 = {"b": 2, "a": 1}
d3 = {"a": 1, "b": 3}

print(d1 == d2)  # True (order doesn't matter)
print(d1 == d3)  # False

######################################################### 14 Removing duplicates

d = {"a": 1, "b": 2, "c": 1}
unique_dict = {}
for k, v in d.items():
    if v not in unique_dict.values():
        unique_dict[k] = v
# Output: {'a': 1, 'b': 2}


# Methods
# Method	        Description
# clear()	        Removes all the elements from the dictionary
# copy()	        Returns a copy of the dictionary
# fromkeys()	    Returns a dictionary with the specified keys and value
# get()	            Returns the value of the specified key
# items() 	        Returns a list containing a tuple for each key value pair
# keys()	        Returns a list containing the dictionary's keys
# pop()	            Removes the element with the specified key
# popitem()	        Removes the last inserted key-value pair
# setdefault()	    Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	        Updates the dictionary with the specified key-value pairs
# values()	        Returns a list of all the values in the dictionary