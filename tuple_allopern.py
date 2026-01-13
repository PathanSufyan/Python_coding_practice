

# | Feature    | List  | Tuple | Set   | Dictionary       |
# | ---------- | ----- | ----- | ----- | ---------------- |
# | Ordered    | ✅     | ✅     | ❌\*   | ✅                |
# | Mutable    | ✅     | ❌     | ✅     | ✅                |
# | Duplicates | ✅     | ✅     | ❌     | Keys ❌, Values ✅ |
# | Indexing   | ✅     | ✅     | ❌     | Keys used        |
# | Syntax     | `[ ]`  | `( )`  | `{ }`   | `{key: value}`   |


# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.()
# Tuple items are ordered, unchangeable, and allow duplicate values.
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# Tuple items can be of any data type:


# 🎯 Why Use Tuples?
# ✅ Data Integrity: Since tuples are immutable, they ensure that data cannot be altered accidentally.
# ✅ Performance: Tuples use less memory and are faster than lists.
# ✅ Hashable: Can be used as keys in dictionaries and elements in sets (if all items inside are immutable).
# ✅ Return Multiple Values: Commonly used to return multiple values from functions.


# 🛠 Real-World Use Cases
# Returning multiple values from a function:
def get_stats():
    return (100, 200)

# Storing coordinate pairs, e.g. (x, y) = (10, 20)
# Using tuples as dictionary keys:
points = {(0, 0): "Origin", (1, 2): "Point A"}

# 🚫 Limitations
# Cannot change, append, or remove elements.
# Not suitable if you need to modify data frequently.

# ✅ When to Use Tuples
# You want read-only data.
# You need better performance (faster than lists).
# You need a hashable type (e.g., dictionary keys).
# You want to return multiple values from a function.

example = (1, 2, 3)

############################################################# Create a Tuple
my_tuple = (10, 20, 30)
empty_tuple = ()
single_element = (5,)  # Note the comma!

####################################################### Update Tuple (Workaround) using convert it into list
my_tuple = (1, 2, 3)
temp_list = list(my_tuple)
temp_list[1] = 20
my_tuple = tuple(temp_list)

############################################################# Delete Tuple
my_tuple = (1, 2, 3)
del my_tuple  # Deletes entire tuple

############################################################# Copy a Tuple
original = (1, 2, 3)
copy_tuple = original[:]  # or just use copy_tuple = original

############################################################# Sort Tuple (Forward, Reverse)
t = (5, 2, 9, 1)
sorted_forward = tuple(sorted(t))
sorted_reverse = tuple(sorted(t, reverse=True))

############################################################# Looping Over Tuple
for item in my_tuple:
    print(item)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

############################################################# Accessing Elements
print(my_tuple[0])      # First element
print(my_tuple[-1])     # Last element
print(my_tuple[2:5])
print(my_tuple[:4])
print(my_tuple[2:])
print(my_tuple[-4:-1])



############################################################## Highest and Lowest Value
print(max(my_tuple))
print(min(my_tuple))

############################################################## Merging Two Tuples
t1 = (1, 2)
t2 = (3, 4)
merged = t1 + t2

############################################################## Convert to Other Data Types
my_tuple = (1, 2, 3)

# To list
as_list = list(my_tuple)

# To set
as_set = set(my_tuple)

# To string
as_string = str(my_tuple)


############################################################### Searching in Tuple
print(2 in my_tuple)          # True/False
print(my_tuple.index(2))      # Get index of 2

###############################################################Comparing Tuples
a = (1, 2, 3)
b = (1, 2, 4)
print(a == b)   # False
print(a < b)    # True (compares element-wise)

################################################################ Remove Duplicates from Tuple
t = (1, 2, 2, 3, 1)
unique = tuple(set(t))  # Order may change


############################################################### Tuple Methods
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

