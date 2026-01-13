######################################################## List Methonds ################################################################
# 1 Method	Description
# 2 append()	Adds an element at the end of the list
# 3 clear()	Removes all the elements from the list
# 4 copy()	Returns a copy of the list
# 5 count()	Returns the number of elements with the specified value
# 6 extend()	Add the elements of a list (or any iterable), to the end of the current list (list, tuple,set and dictionary)
# 7 index()	Returns the index of the first element with the specified value
# 8 insert()	Adds an element at the specified position
# 9 pop()	Removes the element at the specified position
# 10 remove()	Removes the item with the specified value
# 11 reverse()	Reverses the order of the list
# 12 sort()	Sorts the list
# 13 list() to create the list

# | Feature    | List  | Tuple | Set       | Dictionary       |
# | ---------- | ----- | ----- | -----     | ---------------- |
# | Ordered    | ✅     | ✅     | ❌\*   | ✅                |
# | Mutable    | ✅     | ❌     | ✅     | ✅                |
# | Duplicates | ✅     | ✅     | ❌     | Keys ❌, Values ✅ |
# | Indexing   | ✅     | ✅     | ❌     | Keys used        |
# | Syntax     | `[ ]`  | `( )`  | `{ }`   | `{key: value}`   |

########################################### In how many ways we can create the lists #################################################
#######################################################################################################################################


### **1. Using Square Brackets**
my_list = [1, 2, 3, 4]

### **2. Using `list()` Constructor**
my_list = list((1, 2, 3, 4))  # From a tuple
my_list = list("hello")  # From a string

### **3. Using List Comprehension**
my_list = [x ** 2 for x in range(5)]

### **4. Using `range()` with `list()`**
my_list = list(range(10))

### **5. Using `split()` on Strings**
my_list = "apple,banana,cherry".split(",")

### **6. Reading from a File**
with open('file.txt') as f:
    my_list = f.readlines()

### **7. Using Loops**
my_list = []
for i in range(5):
    my_list.append(i)

### **8. Using `map()` Function**
my_list = list(map(int, ["1", "2", "3"]))

### **9. Using `*` Operator for Repetition**
my_list = [0] * 5  # [0, 0, 0, 0, 0]

### **10. Using `copy()` or `[:]`**
original = [1, 2, 3]
copy1 = original[:]
copy2 = original.copy()

### **11. From a Set or Dictionary**
my_list = list({1, 2, 3})
my_list = list({'a': 1, 'b': 2}.keys())  # or .values(), .items()

######################################### In how many ways we can add values to list ##################################################
#######################################################################################################################################

## 🔚 **1. `append()` – Add a single item at the end**
lst = [1, 2]
lst.append(3)
# [1, 2, 3]


## 🧩 **2. `extend()` – Add multiple items (from iterable) at the end**
lst = [1, 2]
lst.extend([3, 4])
# [1, 2, 3, 4]


## 📍 **3. `insert(index, value)` – Add at a specific position**
lst = [1, 2, 4]
lst.insert(2, 3)
# [1, 2, 3, 4]


## ➕ **4. `+=` Operator – Similar to `extend()`**
lst = [1, 2]
lst += [3, 4]
# [1, 2, 3, 4]


## ⛓️ **5. List Concatenation – Using `+` Operator**
lst = [1, 2]
lst = lst + [3, 4]
# [1, 2, 3, 4]


## ♻️ **6. List Comprehension – Add conditionally or dynamically**
lst = [x for x in range(5)]
# [0, 1, 2, 3, 4]


## 🔁 **7. Using a Loop – Append multiple items manually**
lst = []
for i in range(5):
    lst.append(i)

## 📤 **8. Unpacking with `*` in Concatenation**
a = [1, 2]
b = [3, 4]
lst = [*a, *b]
# [1, 2, 3, 4]


## 🧱 **9. `slice assignment` – Insert multiple values at any index**
lst = [1, 5]
lst[1:1] = [2, 3, 4]  # Insert at index 1
# [1, 2, 3, 4, 5]


## 🧬 **10. `collections.deque().appendleft()` – Add to the beginning (alternative structure)**
from collections import deque

d = deque([2, 3])
d.appendleft(1)
lst = list(d)
# [1, 2, 3]


### ✅ Summary Table:

# | Method               | Adds | To        | Example                      |
# | -------------------- | ---- | --------- | ---------------------------- |
# | `append(x)`          | 1    | End       | `lst.append(10)`             |
# | `extend(iterable)`   | Many | End       | `lst.extend([4,5])`          |
# | `insert(i, x)`       | 1    | Specific  | `lst.insert(1, 99)`          |
# | `+=`                 | Many | End       | `lst += [6,7]`               |
# | `+`                  | Many | New list  | `lst = lst + [8,9]`          |
# | List comprehension   | Many | New list  | `[x for x in range(5)]`      |
# | Loop + append        | Many | End       | `for i in ...: lst.append()` |
# | `*` unpacking        | Many | New list  | `[*a, *b]`                   |
# | Slice assignment     | Many | Anywhere  | `lst[1:1] = [a, b]`          |
# | `deque.appendleft()` | 1    | Beginning | Alternative structure        |


######################################### In how many ways we can Update values to list #################################################
########################################################################################################################################


## 🔧 **1. Update by Index**
# Update a single element using its index.

lst = [1, 2, 3]
lst[1] = 99
# [1, 99, 3]


## 🔗 **2. Update a Slice**
# Change multiple elements at once.

lst = [1, 2, 3, 4]
lst[1:3] = [20, 30]
# [1, 20, 30, 4]


## 🔁 **3. Loop through List with Index**
# Update conditionally or transform each value.

lst = [1, 2, 3]
for i in range(len(lst)):
    lst[i] *= 2
# [2, 4, 6]


## 🧠 **4. List Comprehension (Transform All Elements)**
# Creates a new list, but can be reassigned to the same variable.

lst = [1, 2, 3]
lst = [x * 10 for x in lst]
# [10, 20, 30]


## 📊 **5. Using `enumerate()` for Index + Value**
lst = [1, 2, 3]
for i, val in enumerate(lst):
    lst[i] = val + 100
# [101, 102, 103]


## 📍 **6. Update Nested List Values**
lst = [[1, 2], [3, 4]]
lst[1][0] = 99
# [[1, 2], [99, 4]]


## 🧪 **7. Update Based on Condition**
lst = [5, 10, 15]
lst = [x if x < 10 else x + 1 for x in lst]
# [5, 10, 16]


## 🧩 **8. Use `map()` to Apply a Function**
lst = [1, 2, 3]
lst = list(map(lambda x: x * 2, lst))
# [2, 4, 6]


## 🧱 **9. Update with a Dictionary Mapping**
lst = ['a', 'b', 'c']
replace_map = {'a': 'x', 'b': 'y'}
lst = [replace_map.get(x, x) for x in lst]
# ['x', 'y', 'c']


## 🔄 **10. Using `numpy` Arrays for Element-Wise Update**
import numpy as np

arr = np.array([1, 2, 3])
arr += 10
lst = arr.tolist()
# [11, 12, 13]


### ✅ Summary Table

# | Method                    | Use Case                              |
# | ------------------------- | ------------------------------------- |
# | `lst[i] = x`              | Update single value                   |
# | `lst[i:j] = [...]`        | Update multiple values via slicing    |
# | `for i in range(...)`     | Manual update with index              |
# | List comprehension        | Efficient and readable transformation |
# | `enumerate()`             | When you need index and value         |
# | Nested access `lst[i][j]` | For nested/matrix structures          |
# | Conditional update        | Update only matching values           |
# | `map()`                   | Functional programming style          |
# | Mapping with dict         | Replace values with lookups           |
# | `numpy` operations        | Fast updates on numerical data        |


# | Rank | Method                                     | Performance                              | Notes                                             |
# | ---- | ------------------------------------------ | ---------------------------------------- | ------------------------------------------------- |
# | 🥇 1 | `for i in range(len(lst)):`                | ✅ **Fastest** (in-place)                 | In-place modification; avoids creating new lists  |
# | 🥈 2 | `enumerate()` loop                         | ✅ Fast                                   | Similar to above, but more readable               |
# | 🥉 3 | `list comprehension`                       | ⚠️ Fast (creates new list)               | Very fast, but creates a **new list**             |
# | 4    | `map()` + `list()`                         | ⚠️ Fast (new list)                       | Functional style; fast for simple transformations |
# | 5    | `numpy` operations                         | 🚀 Very fast for **large numeric lists** | Requires NumPy; best for numeric arrays           |
# | 6    | `slice assignment`                         | ⚠️ Efficient but specific use            | Works great for range updates                     |
# | 7    | `dictionary mapping` in list comprehension | 🐢 Slower for large dicts                | Slower due to `get()` lookup cost                 |
# | 8    | Nested list updates                        | 🐢 Slower (due to double indexing)       | Costlier for deep or large nested structures      |


# 🧠 Understanding In-Place vs New List Updates
# | Method                                    | Updates Original (In-Place)? | Explanation                                                   |
# | ----------------------------------------- | ---------------------------- | ------------------------------------------------------------- |
# | `lst[i] = value`                          | ✅ Yes                        | Direct assignment to a specific index                         |
# | `lst[i:j] = [...]`                        | ✅ Yes                        | Slice assignment modifies the original list                   |
# | `for i in range(len(lst)):`               | ✅ Yes                        | Each element is updated directly by index                     |
# | `for i, val in enumerate(lst):`           | ✅ Yes                        | Modifies values in-place using index                          |
# | `lst.insert(i, value)`                    | ✅ Yes                        | Adds item to list in-place                                    |
# | `lst.append(value)` / `lst.extend([...])` | ✅ Yes                        | Adds elements in-place                                        |
# | `del lst[i]` or `pop()`                   | ✅ Yes                        | Removes element from the original list                        |
# | `list comprehension`                      | ❌ No                         | Creates a new list and reassigns it                           |
# | `lst = [x if ... else ... for x in lst]`  | ❌ No                         | Creates a new list (even if stored in the same variable name) |
# | `lst = list(map(...))`                    | ❌ No                         | Produces a new list object                                    |
# | `lst = lst + [value]`                     | ❌ No                         | New list object is created                                    |
# | `lst += [value]`                          | ✅ Yes (usually)              | In-place for lists (but not for all types)                    |
# | `numpy_array += value`                    | ✅ Yes                        | In-place for NumPy arrays                                     |
# | `deque[i] = value` or `appendleft()`      | ✅ Yes                        | In-place for deques                                           |
# | `lst = sorted(lst)`                       | ❌ No                         | New sorted list is returned                                   |
# | `lst.sort()`                              | ✅ Yes                        | Sorts in-place                                                |


# Replacing the list values

lst = [1, 2, 3]
lst = list(map(lambda x: x * 2, lst))
# [2, 4, 6]

lst = ['apple', 'banana']
lst = [x.replace('a', '@') for x in lst]
# ['@pple', 'b@n@n@']


######################################### In how many ways we can Delete values to list #################################################
#########################################################################################################################################

## 🧹 **1. Delete by Index (Using `del`)**
lst = [10, 20, 30]
del lst[1]
# [10, 30]


## 🗑️ **2. Delete by Index (Using `pop()`)**
# Removes and returns the item at the given index.

lst = [10, 20, 30]
lst.pop(1)
# [10, 30]

# If no index is provided, it deletes the **last item**.

lst.pop()
# Removes last item


## ❌ **3. Delete by Value (Using `remove()`)**
# Removes **first occurrence** of the specified value.

lst = [10, 20, 30, 20]
lst.remove(20)
# [10, 30, 20]


## 🔁 **4. Delete by Condition (List Comprehension)**
# Create a new list that **excludes certain elements**.

lst = [1, 2, 3, 4, 5]
lst = [x for x in lst if x != 3]
# [1, 2, 4, 5]


## 🔄 **5. Delete by Condition (In-place using Loop + `del`)**
lst = [1, 2, 3, 4, 5]
for i in reversed(range(len(lst))):
    if lst[i] == 3:
        del lst[i]
# [1, 2, 4, 5]


## 📏 **6. Delete Multiple Items by Slice**
lst = [0, 1, 2, 3, 4, 5]
del lst[2:5]
# [0, 1, 5]


## ♻️ **7. Clear Entire List (`clear()`)**
# Removes all elements.

lst = [1, 2, 3]
lst.clear()
# []


## 🧮 **8. Delete All Occurrences of a Value**
lst = [1, 2, 2, 3, 2]
lst = [x for x in lst if x != 2]
# [1, 3]


## 🔍 **9. Delete by Index List**
lst = ['a', 'b', 'c', 'd']
indices_to_remove = [1, 3]
lst = [x for i, x in enumerate(lst) if i not in indices_to_remove]
# ['a', 'c']


## 📚 **10. Delete Using `filter()` (Advanced)**
lst = [1, 2, 3, 4]
lst = list(filter(lambda x: x % 2 == 0, lst))  # Keep evens
# [2, 4]


## 🧠 **11. Delete in Nested Lists**
lst = [[1, 2], [3, 4]]
del lst[1][0]
# [[1, 2], [4]]


## ✅ Summary Table

# | Method                 | Deletes In-Place? | Description                            |
# | ---------------------- | ----------------- | -------------------------------------- |
# | `del lst[i]`           | ✅ Yes             | By index                               |
# | `lst.pop(i)`           | ✅ Yes             | By index (returns value)               |
# | `lst.remove(val)`      | ✅ Yes             | By value (first match)                 |
# | `del lst[i:j]`         | ✅ Yes             | By slice                               |
# | `lst.clear()`          | ✅ Yes             | Clears entire list                     |
# | List comprehension     | ❌ No              | Returns new list without certain items |
# | Loop + `del` (reverse) | ✅ Yes             | Conditional delete in-place            |
# | `filter()`             | ❌ No              | Functional delete (returns new list)   |
# | Nested list delete     | ✅ Yes             | Deletes from sublists                  |
# | `lst = []`             | ❌ (rebinds list)  | Replaces with a new empty list         |


######################################### In how many ways we can search values to list #################################################
#########################################################################################################################################

### ✅ 1. **Using `in` keyword (check existence)**
my_list = [10, 20, 30, 40]
if 20 in my_list:
    print("Found")
else:
    print("Not found")

### ✅ 2. **Using `.index()` (get index of first occurrence)**
my_list = [10, 20, 30, 40]
index = my_list.index(30)  # Returns 2
print("Index:", index)
# > ⚠️ Raises `ValueError` if the element is not found.


### ✅ 3. **Using `for` loop (custom condition or multiple matches)**
my_list = [1, 3, 5, 7, 9]
target = 5
for i, value in enumerate(my_list):
    if value == target:
        print(f"Found {target} at index {i}")

### ✅ 4. **Using list comprehension (find all matches)**
my_list = [1, 2, 3, 2, 4, 2]
indices = [i for i, x in enumerate(my_list) if x == 2]
print("Indices of 2:", indices)

### ✅ 5. **Using `filter()` with a condition**
my_list = ['apple', 'banana', 'cherry']
result = list(filter(lambda x: 'a' in x, my_list))
print(result)  # ['apple', 'banana']

### 🔹 **1. Check if an element exists**
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Yes, banana is in the list")

### 🔹 **2. Get index of an element (first occurrence)**
numbers = [4, 5, 6, 7, 8]
try:
    idx = numbers.index(6)
    print("Index of 6:", idx)
except ValueError:
    print("Element not found")

### 🔹 **3. Find all indices of an element**
nums = [1, 2, 3, 2, 4, 2]
indices = [i for i, x in enumerate(nums) if x == 2]
print("2 appears at indices:", indices)

### 🔹 **4. Find all elements greater than a value**
nums = [10, 20, 30, 40, 15]
result = [x for x in nums if x > 20]
print("Numbers greater than 20:", result)

### 🔹 **5. Search strings that contain a letter**
words = ["dog", "cat", "cow", "duck"]
filtered = [word for word in words if "d" in word]
print("Words with 'd':", filtered)

### 🔹 **6. Search dictionaries inside a list**
users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 25}
]

result = [user for user in users if user["age"] == 25]
print("Users aged 25:", result)

### 🔹 **7. Find the first matching element with a condition**
nums = [3, 6, 9, 12]
match = next((x for x in nums if x > 5), None)
print("First number > 5:", match)

### 🔹 **8. Count occurrences of an element**
items = ["a", "b", "a", "c", "a"]
count = items.count("a")
print("'a' appears", count, "times")

### 🔹 **9. Search case-insensitively in list of strings**
names = ["Alice", "Bob", "Charlie"]
search_name = "alice"
found = any(name.lower() == search_name.lower() for name in names)
print("Found (case-insensitive)?", found)

### 🔹 **10. Filter elements using `filter()` and lambda**
nums = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers:", even_numbers)

## ✅ 1. **Search in Nested Lists**
### 🔍 Find element inside a list of lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Find all rows where 5 appears
rows_with_5 = [i for i, row in enumerate(matrix) if 5 in row]
print("5 found in rows:", rows_with_5)


## ✅ 2. **Search in List of Custom Objects**
### 🎯 Example: Find a student with a specific name
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


students = [
    Student("Alice", 85),
    Student("Bob", 90),
    Student("Charlie", 85)
]

# Find students with grade 85
matches = [s for s in students if s.grade == 85]
for s in matches:
    print(f"Student: {s.name}, Grade: {s.grade}")

## ✅ 3. **Search Using Regular Expressions (Regex)**

### 🔎 Find all strings that start with "a" or contain digits
import re

data = ["apple", "banana", "a123", "dog", "cat7"]

# Words starting with 'a'
starts_with_a = [word for word in data if re.match(r'^a', word)]
print("Start with 'a':", starts_with_a)

# Words containing digits
with_digits = [word for word in data if re.search(r'\d', word)]
print("Contain digits:", with_digits)

## ✅ 4. **Search in a Nested Dictionary List**
### 🔍 Find all users from a specific city
users = [
    {"name": "John", "address": {"city": "New York"}},
    {"name": "Jane", "address": {"city": "Chicago"}},
    {"name": "Jake", "address": {"city": "New York"}},
]

ny_users = [u for u in users if u["address"]["city"] == "New York"]
print("Users in New York:", ny_users)

## ✅ 5. **Search in a Mixed Data List**

### 🔄 Filter only integers from a mixed list
mixed = [1, "hello", 2.5, 3, "world", True]

ints_only = [x for x in mixed if isinstance(x, int) and not isinstance(x, bool)]
print("Integers only:", ints_only)
# > 🔎 `isinstance(x, int)` includes `True` and `False`, so we exclude `bool` explicitly.


######################################### In how many ways we can filter values to list #################################################
#########################################################################################################################################

# Example: filter even numbers
numbers = [1, 2, 3, 4, 5, 6]
evens = [x for x in numbers if x % 2 == 0]
print(evens)  # Output: [2, 4, 6]

# Same example using filter and lambda
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6]

people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

over_30 = [p for p in people if p["age"] > 30]
print(over_30)  # [{'name': 'Charlie', 'age': 35}]

#####
items = [1, 2, 2, 3, 4, 4, 5]
unique_items = list(set(items))
print(unique_items)  # Order may not be preserved

######################################### In how many ways we can sort values to list #################################################
#########################################################################################################################################

## ✅ 1. **Using `sorted()` (Returns a new list)**
numbers = [4, 2, 9, 1]
sorted_list = sorted(numbers)
print(sorted_list)  # [1, 2, 4, 9]

## ✅ 2. **Using `.sort()` (Sorts the list in-place)**
numbers = [4, 2, 9, 1]
numbers.sort()
print(numbers)  # [1, 2, 4, 9]

## ✅ 3. **Sort in Descending Order**
nums = [5, 1, 7, 3]
print(sorted(nums, reverse=True))  # [7, 5, 3, 1]

## ✅ 4. **Sort Strings Alphabetically**
words = ["banana", "apple", "cherry"]
print(sorted(words))  # ['apple', 'banana', 'cherry']

## ✅ 5. **Case-Insensitive String Sort**
words = ["banana", "Apple", "cherry"]
sorted_words = sorted(words, key=lambda x: x.lower())
print(sorted_words)  # ['Apple', 'banana', 'cherry']

## ✅ 6. **Sort by Length of Strings**
words = ["apple", "fig", "banana"]
print(sorted(words, key=len))  # ['fig', 'apple', 'banana']

## ✅ 7. **Sort List of Tuples by Second Element**
pairs = [(1, 3), (2, 1), (4, 2)]
print(sorted(pairs, key=lambda x: x[1]))  # [(2, 1), (4, 2), (1, 3)]

## ✅ 8. **Sort List of Dictionaries by a Field**
users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 30}
]

sorted_users = sorted(users, key=lambda x: x["age"])
print(sorted_users)

## ✅ 9. **Sort with `operator` Module**

from operator import itemgetter

users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 30}
]

print(sorted(users, key=itemgetter("age")))


## ✅ 10. **Sort Custom Objects**
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __repr__(self):
        return f"{self.name}: {self.marks}"


students = [Student("Alice", 88), Student("Bob", 75), Student("Charlie", 92)]

sorted_students = sorted(students, key=lambda s: s.marks)
print(sorted_students)

## ✅ 11. **Stable Sort (Python's sort is stable)**
# Useful when you sort by one field, then by another.
people = [("Alice", 25), ("Bob", 25), ("Charlie", 20)]
# Sort by age, then by name
sorted_people = sorted(people, key=lambda x: (x[1], x[0]))
print(sorted_people)

# Let me show you **3 common ways to manually sort a list using loops**:

## ✅ 1. **Bubble Sort (Beginner-friendly sorting using loop)**
nums = [5, 2, 9, 1, 5, 6]

for i in range(len(nums)):
    for j in range(0, len(nums) - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print("Sorted list:", nums)
# > 🔄 This compares each pair and "bubbles" the largest to the end. Easy but not efficient (O(n²)).


## ✅ 2. **Selection Sort**
nums = [64, 25, 12, 22, 11]

for i in range(len(nums)):
    min_index = i
    for j in range(i + 1, len(nums)):
        if nums[j] < nums[min_index]:
            min_index = j
    nums[i], nums[min_index] = nums[min_index], nums[i]

print("Sorted list:", nums)
# > ✅ Finds the minimum element and puts it at the beginning. Also O(n²).


## ✅ 3. **Insertion Sort**
nums = [12, 11, 13, 5, 6]

for i in range(1, len(nums)):
    key = nums[i]
    j = i - 1
    while j >= 0 and key < nums[j]:
        nums[j + 1] = nums[j]
        j -= 1
    nums[j + 1] = key

print("Sorted list:", nums)

### ✨ Summary of Manual Sorting (via Loop):

# | Algorithm      | Time Complexity  | Best For                     |
# | -------------- | ---------------- | ---------------------------- |
# | Bubble Sort    | O(n²)            | Easy to understand           |
# | Selection Sort | O(n²)            | Simple logic                 |
# | Insertion Sort | O(n²), O(n) best | Small or nearly sorted lists |


### 📌 Real Tip:
# Use manual sorting only for learning. In real-world Python:

sorted_list = sorted(my_list)  # Preferred for readability and performance

######################################### In how many ways we can slice values to list #################################################
#########################################################################################################################################


### 🧠 Basic Slice Syntax:
list[start:stop:step]

# * `start`: index to begin (inclusive)
# * `stop`: index to end (exclusive)
# * `step`: step size (can be negative)


## ✅ 1. **Slice First N Elements**
lst = [0, 1, 2, 3, 4, 5]
print(lst[:3])  # [0, 1, 2]

## ✅ 2. **Slice From N to End**
print(lst[3:])  # [3, 4, 5]

## ✅ 3. **Slice a Middle Range**
print(lst[2:5])  # [2, 3, 4]

## ✅ 4. **Slice With Step**
print(lst[::2])  # [0, 2, 4]

## ✅ 5. **Reverse the List**
print(lst[::-1])  # [5, 4, 3, 2, 1, 0]

## ✅ 6. **Every Third Element From Index 1**
print(lst[1::3])  # [1, 4]

## ✅ 7. **Negative Indexing (From End)**
print(lst[-3:])  # Last 3 elements: [3, 4, 5]
print(lst[-4:-1])  # [2, 3, 4]

## ✅ 8. **Exclude First and Last Elements**
print(lst[1:-1])  # [1, 2, 3, 4]

## ✅ 9. **Copy the List Using Slice**
copy = lst[:]
print(copy)  # [0, 1, 2, 3, 4, 5]

## ✅ 10. **Slice and Assign to Modify Part**
lst[1:3] = ['a', 'b']
print(lst)  # [0, 'a', 'b', 3, 4, 5]

## ✅ 11. **Remove Elements Using Slice Delete**
del lst[1:4]
print(lst)  # After deletion: [0, 4, 5]

## ✅ 12. **Slicing with `slice()` Function**
s = slice(1, 4)
print(lst[s])  # Same as lst[1:4]

### ✨ Bonus: Slice Multidimensional Lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Get second column
column = [row[1] for row in matrix]
print(column)  # [2, 5, 8]

### 📌 Summary Table

# | Pattern              | Syntax            | Output               |
# | -------------------- | ----------------- | -------------------- |
# | First 3 items        | `lst[:3]`         | `[0, 1, 2]`          |
# | Last 3 items         | `lst[-3:]`        | `[3, 4, 5]`          |
# | Middle slice         | `lst[1:4]`        | `[1, 2, 3]`          |
# | Every 2nd element    | `lst[::2]`        | `[0, 2, 4]`          |
# | Reverse list         | `lst[::-1]`       | `[5, 4, 3, 2, 1, 0]` |
# | Slice with `slice()` | `lst[slice(1,4)]` | `[1, 2, 3]`          |


#################################### In how many ways we can remove duplicates from list ################################################
#########################################################################################################################################

## ✅ 1. **Using `set()` (Fastest, but **does not preserve order**)**
my_list = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(my_list))
print(unique)  # Output: [1, 2, 3, 4, 5] (order may change)

## ✅ 2. **Using `dict.fromkeys()` (Preserves order, Python ≥3.7)**
my_list = [1, 2, 2, 3, 4, 4, 5]
unique = list(dict.fromkeys(my_list))
print(unique)  # Output: [1, 2, 3, 4, 5]

## ✅ 3. **Using Loop with a `seen` Set (Preserves Order)**
my_list = [1, 2, 2, 3, 4, 4, 5]
seen = set()
unique = []

for item in my_list:
    if item not in seen:
        seen.add(item)
        unique.append(item)

print(unique)  # Output: [1, 2, 3, 4, 5]

## ✅ 4. **Using List Comprehension with Set (One-liner with order preserved)**
my_list = [1, 2, 2, 3, 4, 4, 5]
seen = set()
unique = [x for x in my_list if not (x in seen or seen.add(x))]
print(unique)  # Output: [1, 2, 3, 4, 5]

## ✅ 5. **Using Pandas (For large or complex datasets)**
import pandas as pd

my_list = [1, 2, 2, 3, 4, 4, 5]
unique = pd.Series(my_list).drop_duplicates().tolist()
print(unique)  # Output: [1, 2, 3, 4, 5]

## ✅ 6. **Using `collections.OrderedDict` (For older Python versions)**
from collections import OrderedDict

my_list = [1, 2, 2, 3, 4, 4, 5]
unique = list(OrderedDict.fromkeys(my_list))
print(unique)  # Output: [1, 2, 3, 4, 5]

## ✅ 7. **Removing Duplicates in Nested Lists or Objects (Advanced)**
# For a list of lists or dictionaries, you'll need to use `json.dumps`, `frozenset`, or manual checks.
# Example: remove duplicate lists:

import json

nested = [[1, 2], [3, 4], [1, 2]]
unique = list(map(json.loads, set(map(json.dumps, nested))))
print(unique)  # [[1, 2], [3, 4]]

### 📌 Summary

# | Method                            | Preserves Order | Best For                   |
# | --------------------------------- | --------------- | -------------------------- |
# | `set()`                           | ❌               | Speed, unordered lists     |
# | `dict.fromkeys()`                 | ✅               | Clean and Pythonic         |
# | Loop with `seen` set              | ✅               | Full control               |
# | List comprehension + set          | ✅               | One-liner with logic       |
# | `pandas.Series.drop_duplicates()` | ✅               | Data analysis / pipelines  |
# | `OrderedDict.fromkeys()`          | ✅               | Python < 3.7 compatibility |


#################################### In how many ways we can loop over list ###############################################
########################################################################################################################################

# In Python, you can loop through a list in **many different ways**, depending on what you need (index, value, both, reverse,
# condition, etc.). Below are the **most common and powerful techniques**:


## ✅ 1. **Basic `for` Loop (Direct Element Access)**
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

## ✅ 2. **Using `range()` with Index**
for i in range(len(fruits)):
    print(fruits[i])

## ✅ 3. **Using `enumerate()` (Get Index + Value)**
for index, fruit in enumerate(fruits):
    print(index, fruit)

## ✅ 4. **Using `while` Loop**
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

## ✅ 5. **Loop in Reverse (`reversed()`)**
for fruit in reversed(fruits):
    print(fruit)

## ✅ 6. **Loop with Step Size Using `range(start, end, step)`**
numbers = [10, 20, 30, 40, 50]
for i in range(0, len(numbers), 2):
    print(numbers[i])  # 10, 30, 50

## ✅ 7. **Using List Comprehension (Compact syntax)**
[print(fruit) for fruit in fruits]

## ✅ 8. **Loop with `zip()` (Multiple Lists Together)**
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 95]

for name, score in zip(names, scores):
    print(name, score)


## ✅ 9. **Using `map()` Function**
def shout(word):
    print(word.upper())


list(map(shout, fruits))

## ✅ 10. **Using `filter()` with Loop**
evens = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))
for num in evens:
    print(num)

## ✅ 11. **Using `enumerate()` with `start` parameter**
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

## ✅ 12. **Looping with Condition (Inside Loop)**
for fruit in fruits:
    if 'a' in fruit:
        print(fruit)

## ✅ 13. **Loop in Sorted Order**
for fruit in sorted(fruits):
    print(fruit)

## ✅ 14. **Loop Through List Backwards with Index**
for i in range(len(fruits) - 1, -1, -1):
    print(fruits[i])

## ✅ 15. **Using `itertools` for Advanced Looping**
from itertools import cycle, islice

# Infinite loop (stopped after 5)
for item in islice(cycle(fruits), 5):
    print(item)

### 📌 Summary Table

# | Method                | Use Case                            |
# | --------------------- | ----------------------------------- |
# | `for item in list`    | Simple loop over items              |
# | `for i in range(...)` | Access by index                     |
# | `enumerate()`         | Need index and value                |
# | `zip()`               | Loop over multiple lists            |
# | `while` loop          | Custom loop logic or manual control |
# | `reversed()`          | Loop in reverse                     |
# | `list comprehension`  | One-line loops                      |
# | `sorted()`            | Loop in sorted order                |


## ✅ 1. **Loop Through Nested Lists**

### Example:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for item in row:
        print(item, end=" ")

# > 🔁 Loops through each row, then each item.


## ✅ 2. **Loop Through List of Dictionaries**

### Example:
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35}
]

for person in people:
    print(person["name"], "-", person["age"])

# > 🔑 Access values by keys within each dictionary.


## ✅ 3. **Loop With `break` (Stop early)**
for fruit in ['apple', 'banana', 'mango', 'orange']:
    if fruit == 'mango':
        print("Found mango, stopping loop.")
        break
    print(fruit)

# > 🚫 Stops the loop when a condition is met.


## ✅ 4. **Loop With `continue` (Skip iteration)**
for fruit in ['apple', 'banana', 'mango', 'orange']:
    if fruit == 'banana':
        continue  # Skip banana
    print(fruit)

# > ⏭ Skips that specific iteration but continues the rest.


## ✅ 5. **Loop with Condition Inside Nested Loop**
matrix = [
    [1, 0, 3],
    [0, 5, 6],
    [7, 0, 9]
]

for row in matrix:
    for item in row:
        if item == 0:
            continue  # Skip 0s
        print(item, end=" ")

# > Skips certain values (e.g., `0`) in a nested list.


## ✅ 6. **Using `break` in Nested Loop**
for row in matrix:
    for item in row:
        if item == 5:
            print("Found 5, exiting inner loop.")
            break
        print(item, end=" ")
    print()  # Newline for clarity

## ✅ 7. **Loop With `else` (Loop completed without `break`)**
for num in [1, 2, 3, 4]:
    if num == 5:
        break
else:
    print("Loop completed without breaking.")

# > ✅ The `else` block only runs if the loop wasn’t interrupted by `break`.


### 📌 Summary Table

# | Feature              | Use Case                              |
# | -------------------- | ------------------------------------- |
# | Nested List          | Matrix-style data                     |
# | List of Dictionaries | JSON-like records                     |
# | `break`              | Exit loop early                       |
# | `continue`           | Skip specific iterations              |
# | `else` with loop     | Run logic only if no `break` occurred |


## 🔁 Basic Concept of Double (Nested) Loop
for outer in range(3):  # Outer loop runs 3 times
    for inner in range(2):  # Inner loop runs 2 times for EACH outer loop
        print(f"outer={outer}, inner={inner}")

### 🔎 Output:
# outer=0, inner=0
# outer=0, inner=1
# outer=1, inner=0
# outer=1, inner=1
# outer=2, inner=0
# outer=2, inner=1

# > 🚨 **Important**:
# > For every **1 iteration of the outer loop**, the **inner loop runs completely**.


## ✅ Use Case 1: **Looping Through a 2D List (Matrix)**
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for item in row:
        print(item, end=' ')

### Output:
# 1 2 3 4 5 6 7 8 9


# > 🧠 First loop picks a row → second loop picks each element in that row.

## ✅ Use Case 2: **Creating a Pattern**
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i},{j})", end=' ')
    print()  # Newline after each row

### Output:
# (1,1) (1,2) (1,3)
# (2,1) (2,2) (2,3)
# (3,1) (3,2) (3,3)


## ✅ Use Case 3: **Comparing Every Pair in Two Lists**
colors = ['red', 'green']
shapes = ['circle', 'square']

for color in colors:
    for shape in shapes:
        print(f"{color} {shape}")

### Output:
# red circle
# red square
# green circle
# green square


## ✅ Use Case 4: **Building Multiplication Table**
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=' ')
    print()

### Output:
# 1 2 3
# 2 4 6
# 3 6 9


### 🔁 How It Works (Visually):
# Think of it like this:

for i in [1, 2, 3]:
    for j in [a, b]:
        print(i, j)

# Output:
# 1 a
# 1 b
# 2 a
# 2 b
# 3 a
# 3 b


### 💡 When to Use Double Loops

# * Processing **2D arrays or matrices**
# * Working with **combinations of elements**
# * Building **patterns** or **tables**
# * Comparing all pairs or combinations


##################################
#################################

# Great question! Let's break down what `end=' '` means in Python, especially in the context of `print()`.

## 🧠 By Default: `print()` Adds a Newline (`\n`)

# In Python, the `print()` function **automatically adds a newline** after printing:

print("Hello")
print("World")

### Output:
# Hello
# World


# 👉 This is because the default behavior is:

print("something", end='\n')

## ✅ What `end=' '` Does

# When you use:
print("Hello", end=' ')

# You are **telling Python**:
# > After printing "Hello", **don't go to the next line** — instead, **end the print with a space** (`' '`).


print("Hello", end=' ')
print("World")

### Output:
# Hello World

# ✅ **No newline** between "Hello" and "World" — just a space.

## 📌 More Examples

### 1. Custom Separator:
for i in range(1, 4):
    print(i, end=' ')

# Output:
# 1 2 3

### 2. No Space or Comma:
for i in range(1, 4):
    print(i, end=',')

# Output:
# 1,2,3,


### 3. Same Line Without Space:
for char in 'abc':
    print(char, end='')

# Output:
# abc


## 🎯 Why Use `end=' '`?

# * To print things on **the same line**
# * To format output (like a table, CSV, or pattern)
# * To avoid automatic newline


## 📌 Summary

# | Syntax               | What It Does               |
# | -------------------- | -------------------------- |
# | `print(x)`           | Adds newline after `x`     |
# | `print(x, end=' ')`  | Adds space instead         |
# | `print(x, end='')`   | Adds **nothing** after `x` |
# | `print(x, end=', ')` | Adds a comma + space       |


# Would you like to try examples where we:

# * Print lists in a single line?
# * Build patterns using `end`?
# * Customize output like `end=' --> '`?

#################################### In how many ways we can copy list ###############################################
######################################################################################################################################

# Great question! In Python, there are **several ways to copy a list**, depending on whether you want a **shallow copy** or a **deep copy**.


## ✅ 1. **Using Slicing** (`[:]`) — *Shallow Copy*
original = [1, 2, 3]
copy_list = original[:]

# > 🔁 Creates a new list with the **same values**, but still references inner objects (if any).

## ✅ 2. **Using `list()` Constructor** — *Shallow Copy*
original = [1, 2, 3]
copy_list = list(original)

# > Same as slicing — new list with same elements.

## ✅ 3. **Using `copy.copy()`** — *Shallow Copy*
import copy

original = [1, 2, 3]
copy_list = copy.copy(original)

# > Also performs a shallow copy.

## ✅ 4. **Using `copy.deepcopy()`** — *Deep Copy*
import copy

original = [[1, 2], [3, 4]]
copy_list = copy.deepcopy(original)

# > 🔄 Deep copy copies **nested lists** as well, so changes to inner lists won't affect the original.

## ✅ 5. **Using List Comprehension**
original = [1, 2, 3]
copy_list = [item for item in original]

# > Builds a new list from the old one. Still shallow.

## ✅ 6. **Using `*` Operator Inside `list()`**
original = [1, 2, 3]
copy_list = list([*original])

# > Also shallow copy. Useful in unpacking situations.


## ✅ 7. **Using `copy()` Method (Python 3.3+)**
original = [1, 2, 3]
copy_list = original.copy()

# > Very clean and common for shallow copy.

## ✅ Summary Table

# | Method              | Type     | Supports Nested Copy? | Python Version |
# | ------------------- | -------- | --------------------- | -------------- |
# | `[:]`               | Shallow  | ❌                     | All            |
# | `list(original)`    | Shallow  | ❌                     | All            |
# | `copy.copy()`       | Shallow  | ❌                     | All            |
# | `copy.deepcopy()`   | **Deep** | ✅                     | All            |
# | List Comprehension  | Shallow  | ❌                     | All            |
# | `list([*original])` | Shallow  | ❌                     | 3.x            |
# | `original.copy()`   | Shallow  | ❌                     | Python 3.3+    |


## 📌 Shallow vs Deep Copy Visual:
import copy

a = [[1, 2], [3, 4]]
shallow = a[:]  # Both inner lists shared
deep = copy.deepcopy(a)  # Everything copied

a[0][0] = 100
print(shallow)  # [[100, 2], [3, 4]]
print(deep)  # [[1, 2], [3, 4]]

#################################### In how many ways we can join list ###############################################
######################################################################################################################################

## 🔗 **1. Using `+` Operator (Concatenation)**
a = [1, 2]
b = [3, 4]
result = a + b

# ✅ Output: `[1, 2, 3, 4]`

## 🔗 **2. Using `extend()` Method**
a = [1, 2]
b = [3, 4]
a.extend(b)

# ✅ `a` becomes `[1, 2, 3, 4]`
# ⛔ Modifies the original list (`a`).


## 🔗 **3. Using `*` (Unpacking Operator)**
a = [1, 2]
b = [3, 4]
result = [*a, *b]

# ✅ Output: `[1, 2, 3, 4]`


## 🔗 **4. Using `list()` + `zip()` + List Comprehension (Zipping and Joining)**
a = [1, 2]
b = ['a', 'b']
result = [(x, y) for x, y in zip(a, b)]

# ✅ Output: `[(1, 'a'), (2, 'b')]`
# 🔁 Pairs elements positionally.


## 🔗 **5. Using `itertools.chain()` (Efficient for many lists)**
from itertools import chain

a = [1, 2]
b = [3, 4]
result = list(chain(a, b))

# ✅ Output: `[1, 2, 3, 4]`


## 🔗 **6. Using a Loop**
a = [1, 2]
b = [3, 4]
for item in b:
    a.append(item)

# ✅ `a` becomes `[1, 2, 3, 4]`
# ⛔ Modifies the original list.


## 🔗 **7. Using `join()` (for String Lists Only)**
words = ['Hello', 'World']
result = ' '.join(words)

# ✅ Output: `'Hello World'`

# ⚠️ Works only for lists of strings.


## 🔗 **8. Using List Comprehension**
a = [[1, 2], [3, 4]]
flat = [item for sublist in a for item in sublist]

# ✅ Output: `[1, 2, 3, 4]`
# 🔁 Flattens nested lists.


## 🔗 **9. Using `sum()` for Flat Lists Only**
a = [[1, 2], [3, 4]]
result = sum(a, [])

# ✅ Output: `[1, 2, 3, 4]`
# ⚠️ Works only if sublists are the same type.

## ✅ Summary Table

# | Method                  | Use Case                        | In-Place | Works with Nested? |
# | ----------------------- | ------------------------------- | -------- | ------------------ |
# | `+`                     | Simple merge                    | ❌        | No                 |
# | `.extend()`             | Append another list             | ✅        | No                 |
# | `[*a, *b]`              | Pythonic merge                  | ❌        | No                 |
# | `zip()` + comprehension | Pairing values                  | ❌        | No                 |
# | `itertools.chain()`     | Efficient joining               | ❌        | No                 |
# | `for` + `append()`      | Manual merge                    | ✅        | No                 |
# | `'separator'.join()`    | String list to single string    | ❌        | No (strings only)  |
# | List comprehension      | Flatten nested list             | ❌        | Yes                |
# | `sum(a, [])`            | Quick flatten (not recommended) | ❌        | Yes                |

# Great! Let's go deeper into **joining multiple lists**, **mixed data types**, and **deeply nested lists** with **practical examples**. Here's how you can handle each scenario:

## ✅ 1. **Joining More Than Two Lists**

### ➤ Using `+` operator:
a = [1, 2]
b = [3, 4]
c = [5, 6]
result = a + b + c
print(result)  # [1, 2, 3, 4, 5, 6]

### ➤ Using unpacking (`*`):
lists = [[1, 2], [3, 4], [5, 6]]
result = [*lists[0], *lists[1], *lists[2]]
print(result)  # [1, 2, 3, 4, 5, 6]

### ➤ Using `itertools.chain()`:
from itertools import chain

lists = [[1, 2], [3, 4], [5, 6]]
result = list(chain(*lists))
print(result)  # [1, 2, 3, 4, 5, 6]

## ✅ 2. **Joining Lists with Mixed Data Types**

# If your list contains **different types** like integers and strings, you need to convert all to strings **before using `.join()`**.

### ➤ Using `str()` in list comprehension:
data = [1, 'apple', 3.14, True]
result = ' | '.join(str(x) for x in data)
print(result)  # 1 | apple | 3.14 | True

### ➤ Merging mixed types:
list1 = [1, 2]
list2 = ['a', 'b']
merged = list1 + list2
print(merged)  # [1, 2, 'a', 'b']


## ✅ 3. **Flatten Deeply Nested Lists**

# For multi-level nesting like `[[1, 2], [3, [4, 5]], [6]]`, you need a recursive approach.

### ➤ Using recursion:
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


nested = [[1, 2], [3, [4, 5]], [6]]
flat = flatten(nested)
print(flat)  # [1, 2, 3, 4, 5, 6]

### ➤ Using `itertools.chain` (only for one-level nesting):
from itertools import chain

nested = [[1, 2], [3, 4], [5, 6]]
flat = list(chain.from_iterable(nested))
print(flat)  # [1, 2, 3, 4, 5, 6]

## ✅ Bonus: Join With Custom Separators or Formatting

### ➤ Add comma between elements:
words = ['apple', 'banana', 'mango']
result = ', '.join(words)
print(result)  # apple, banana, mango

### ➤ Add index and format:
items = ['a', 'b', 'c']
for i, item in enumerate(items):
    print(f"{i + 1}. {item}")
# Output:
# 1. a
# 2. b
# 3. c


## ✅ Recap: Best Methods Based on Scenario

# | Situation                  | Best Method                |
# | -------------------------- | -------------------------- |
# | Simple merge               | `+` or `extend()`          |
# | Merge multiple lists       | `*` unpacking or `chain()` |
# | Flatten nested list        | Recursion or `chain()`     |
# | Join strings into sentence | `' '.join()`               |
# | Mixed data types           | `str(x) for x in list`     |
# | Deep nested list           | Custom recursive function  |

#######################################################################################################################
####################### Python - List Comprehension  #################################################################
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# newlist = [expression for item in iterable if condition == True]
# The condition is like a filter that only accepts the items that evaluate to True.
# The iterable can be any iterable object, like a list, tuple, set etc.
# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:

# List comprehension is a concise way to create or transform lists using a single line of code. It is more compact, readable, and often faster than traditional for loops.
# new_list = [expression for item in iterable if condition]
#   expression: What you want to do with each item
#   iterable: Any iterable (like a list, string, range)
#   condition (optional): Filter which items to include

squares = [x ** 2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5, 6]
even = [x for x in numbers if x % 2 == 0]
print(even)  # [2, 4, 6]

fruits = ['apple', 'banana', 'cherry']
upper_fruits = [fruit.upper() for fruit in fruits]
print(upper_fruits)  # ['APPLE', 'BANANA', 'CHERRY']

numbers = [1, 2, 3, 4, 5]
result = [x if x % 2 == 0 else 'odd' for x in numbers]
print(result)  # ['odd', 2, 'odd', 4, 'odd']

result = [x for x in range(10) if x % 3 == 0]


#######################################################################################################################

# Yes! In Python, some **list methods modify the original list in place**,
# meaning they **change the list itself** instead of creating a new one. Here’s a complete list of such methods:


### ✅ **Python List Methods That Modify the Original List (In-Place)**

# | Method                          | Description                                                                          |
# | ------------------------------- | ------------------------------------------------------------------------------------ |
# | `append(x)`                     | Adds element `x` to the end of the list.                                             |
# | `extend(iterable)`              | Adds all elements from an iterable (e.g., list, tuple) to the end of the list.       |
# | `insert(index, x)`              | Inserts element `x` at a specific position.                                          |
# | `remove(x)`                     | Removes the first occurrence of element `x`.                                         |
# | `pop([index])`                  | Removes and returns item at index (last by default).                                 |
# | `clear()`                       | Removes all items from the list.                                                     |
# | `sort(key=None, reverse=False)` | Sorts the list in place.                                                             |
# | `reverse()`                     | Reverses the elements of the list in place.                                          |
# | `*=`, `+=` operators            | These can also modify the list in place when used as `list += [...]` or `list *= 2`. |



### 🔁 Examples

# Original List
fruits = ['apple', 'banana', 'cherry']

# append()
fruits.append('date')  # ['apple', 'banana', 'cherry', 'date']

# extend()
fruits.extend(['elderberry', 'fig'])  # ['apple', ..., 'fig']

# insert()
fruits.insert(1, 'blueberry')  # ['apple', 'blueberry', 'banana', ...]

# remove()
fruits.remove('banana')  # removes first 'banana'

# pop()
fruits.pop()  # removes last item

# clear()
fruits.clear()  # []

# sort()
numbers = [5, 3, 9, 1]
numbers.sort()  # [1, 3, 5, 9]

# reverse()
numbers.reverse()  # [9, 5, 3, 1]


# Let me know if you want the list methods **that do NOT change the original list**
# (i.e., that return a new list instead).

#########################################################################################################################

# Great! Here's a list of **Python list operations/methods that do NOT modify the original list** — instead,
# they return a **new list** or value, leaving the original list unchanged.

### 🚫 Python List Operations That Do NOT Change the Original List

# | Operation / Method   | Description                                 | Returns                         |
# | -------------------- | ------------------------------------------- | ------------------------------- |
# | `sorted(list)`       | Returns a new sorted list.                  | New list                        |
# | `reversed(list)`     | Returns an iterator with reversed elements. | Iterator                        |
# | `list.copy()`        | Returns a shallow copy of the list.         | New list                        |
# | `list[:]`            | Slicing to copy or subset a list.           | New list                        |
# | `list + list`        | List concatenation.                         | New list                        |
# | `list * n`           | Repeats list elements `n` times.            | New list                        |
# | `filter(func, list)` | Filters elements using a function.          | Filter object (convert to list) |
# | `map(func, list)`    | Applies a function to each element.         | Map object (convert to list)    |
# | `list comprehension` | `[x for x in list if ...]`                  | New list                        |
# | `zip(list1, list2)`  | Combines multiple lists.                    | Zip object (convert to list)    |


### ✅ Examples

nums = [5, 3, 1, 4, 2]

# sorted()
new_sorted = sorted(nums)      # [1, 2, 3, 4, 5]
print(nums)                    # [5, 3, 1, 4, 2] → original unchanged

# reversed()
rev = list(reversed(nums))     # [2, 4, 1, 3, 5]

# copy()
copy_list = nums.copy()

# slicing
slice_list = nums[1:4]         # [3, 1, 4]

# list comprehension
squares = [x*x for x in nums]  # [25, 9, 1, 16, 4]

# + and *
double = nums * 2              # [5, 3, 1, 4, 2, 5, 3, 1, 4, 2]
combined = nums + [10, 20]     # [5, 3, 1, 4, 2, 10, 20]


