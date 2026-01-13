# Interview Qustions
# 1 Find the max and min value in the list?
# 2 Remove the duplicates from the list?
# 3 Sort and merge the list?
# 4 Amstrong number?
# 5 Fibonacci series?
# 6 Find the factorial of given number?
# 7 Palendrom?
# 8 Occurance count or count the vowels in the string?
# 9 Make strings every words first character capital?
# 10 Reverse the list or string?
# 11 Swapping ?
# 12 Anagrams?
# 13 Find the first non-repeating character in the string?
# 14 Decorators?
# 15 Find the missing number in the [1,2,4,5,6,7,8,9]? output is 3?
# 16 find the longest and shorted word in the string?

# You can find the **highest** and **lowest** values in a list in Python in several simple ways.
## ✅ **1. Using `max()` and `min()`**

# This is the most direct and Pythonic way.
numbers = [4, 1, 9, -2, 7, 0]

highest = max(numbers)
lowest = min(numbers)

print("Highest:", highest)  # 9
print("Lowest:", lowest)    # -2


## ✅ **2. Using `sorted()`**
# This method **sorts** the list and picks the first and last values:
numbers = [4, 1, 9, -2, 7, 0]
sorted_list = sorted(numbers)

lowest = sorted_list[0]
highest = sorted_list[-1]

print("Highest:", highest)  # 9
print("Lowest:", lowest)    # -2


# ⚠️ Note: This creates a **new sorted list**, so it may not be as efficient as `min()`/`max()` for large lists.


## ✅ **3. Using a Loop (Manual Approach)**
# You can find them manually by looping:
numbers = [4, 1, 9, -2, 7, 0]

highest = numbers[0]
lowest = numbers[0]

for num in numbers:
    if num > highest:
        highest = num
    if num < lowest:
        lowest = num

print("Highest:", highest)  # 9
print("Lowest:", lowest)    # -2


# 🔍 This is useful when you want full control (like tracking positions or using conditions).


## 🚫 What if the list is empty?
numbers = []
# max(numbers) or min(numbers) will raise ValueError

if numbers:
    print(max(numbers), min(numbers))
else:
    print("List is empty.")


## ✅ Summary

# | Method            | Use Case                         | Fast? | Pythonic? |
# | ----------------- | -------------------------------- | ----- | --------- |
# | `max()` / `min()` | Best for simple values           | ✅     | ✅         |
# | `sorted()`        | Good if you need sorted list too | ⚠️    | ✅         |
# | Loop              | Custom logic / conditions needed | ✅     | 🔧 Manual |

################################## Remove duplicate values from the list ##############################################################
######################################################################################################################################

# Great! In Python, there are several ways to **remove duplicate values** from a list depending on whether you want to **preserve order** or not. Here are the most common and effective ways:

## ✅ 1. **Using `set()` (Fastest, but doesn't preserve order)**
my_list = [1, 2, 2, 3, 4, 4, 5]
no_duplicates = list(set(my_list))
print(no_duplicates)

# 🔁 Output: `[1, 2, 3, 4, 5]` (Order may vary)

## ✅ 2. **Using `dict.fromkeys()` (Preserves order, Python ≥ 3.7)**
my_list = [1, 2, 2, 3, 4, 4, 5]
no_duplicates = list(dict.fromkeys(my_list))
print(no_duplicates)

# 🔁 Output: `[1, 2, 3, 4, 5]`

## ✅ 3. **Using a Loop and a Set (Manual, preserves order)**
my_list = [1, 2, 2, 3, 4, 4, 5]
seen = set()
unique = []

for item in my_list:
    if item not in seen:
        unique.append(item)
        seen.add(item)

print(unique)

# 🔁 Output: `[1, 2, 3, 4, 5]`


## ✅ 4. **Using List Comprehension with `not in` (Less efficient for large lists)**
my_list = [1, 2, 2, 3, 4, 4, 5]
unique = []
[unique.append(x) for x in my_list if x not in unique]
print(unique)


# 🔁 Output: `[1, 2, 3, 4, 5]`

# ⚠️ Slower on large datasets compared to using `set()`.


## 🧠 Bonus: Removing Duplicates from a List of Dictionaries
import json

data = [
    {"id": 1}, {"id": 2}, {"id": 1}, {"id": 3}
]

unique = []
seen = set()

for d in data:
    j = json.dumps(d, sort_keys=True)
    if j not in seen:
        seen.add(j)
        unique.append(d)

print(unique)

# 🔁 Output: `[{'id': 1}, {'id': 2}, {'id': 3}]`


## ✅ Summary
# | Method             | Preserves Order | Best For             |
# | ------------------ | --------------- | -------------------- |
# | `set()`            | ❌               | Simple, fast removal |
# | `dict.fromkeys()`  | ✅               | Ordered data         |
# | Loop with `set`    | ✅               | Custom filtering     |
# | List comprehension | ✅               | Small lists          |


# * Remove duplicates **case-insensitively** (e.g., "a" and "A")
# * Remove duplicates **by condition** (like key or index)
# * Remove from **nested or mixed-type lists**

# Great! Let's now explore **advanced and special cases** of removing duplicates in Python. This includes handling:

# 1. ✅ **Case-insensitive duplicates**
# 2. ✅ **List of tuples**
# 3. ✅ **List of dictionaries by specific key**
# 4. ✅ **Nested lists**
# 5. ✅ **Performance notes**

### ✅ 1. **Case-Insensitive Duplicate Removal**

# For lists like `["Apple", "apple", "APPLE"]`:

words = ["Apple", "apple", "APPLE", "Banana", "BANANA"]
unique = []
seen = set()

for word in words:
    word_lower = word.lower()
    if word_lower not in seen:
        seen.add(word_lower)
        unique.append(word)

print(unique)

# 🔁 Output:['Apple', 'Banana']


### ✅ 2. **Remove Duplicates from List of Tuples**
# Tuples are hashable, so this is easy:

pairs = [(1, 2), (3, 4), (1, 2), (5, 6)]
unique = list(set(pairs))
print(unique)

# 🔁 Output (order not guaranteed):

# [(1, 2), (3, 4), (5, 6)]

# To preserve order:
seen = set()
unique = []
for pair in pairs:
    if pair not in seen:
        seen.add(pair)
        unique.append(pair)

print(unique)


### ✅ 3. **Remove Duplicates from List of Dictionaries by Key**

# For a list like:
data = [
    {'id': 1, 'name': 'A'},
    {'id': 2, 'name': 'B'},
    {'id': 1, 'name': 'A'}
]


# Remove duplicates based on `'id'`:
seen = set()
unique = []
for d in data:
    if d['id'] not in seen:
        seen.add(d['id'])
        unique.append(d)

print(unique)

# 🔁 Output:[{'id': 1, 'name': 'A'}, {'id': 2, 'name': 'B'}]


### ✅ 4. **Remove Duplicates from Nested Lists**
# If the list contains sub-lists like this:

nested = [[1, 2], [3, 4], [1, 2]]

# Since lists are unhashable, you can convert them to tuples:
seen = set()
unique = []

for sublist in nested:
    t = tuple(sublist)
    if t not in seen:
        seen.add(t)
        unique.append(sublist)

print(unique)

# 🔁 Output:[[1, 2], [3, 4]]


### ✅ 5. **Performance Notes**

# | Method            | Time Complexity | Best Use Case                |
# | ----------------- | --------------- | ---------------------------- |
# | `set()`           | O(n)            | Simple types (int, str)      |
# | `dict.fromkeys()` | O(n)            | Keep order, simple types     |
# | Loop + `set()`    | O(n)            | Complex filtering/structures |
# | JSON method       | O(n)            | List of dictionaries         |

################################## Number of occurance in the list ###################################################################
######################################################################################################################################

# count words
def count_word_occurrences(s):
    words = s.split()
    freq = {}
    for word in words:
        word = word.lower()  # optional: make case-insensitive
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

text = "This is a test. This test is simple."
result = count_word_occurrences(text)
print(result)

# count alphabets
def count_occurrences(s):
    freq = {}
    for char in s:
        char = char.lower()
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

# Example usage
text = "hello world"
result = count_occurrences(text)
print(result)

{'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

################################## Sort and merge the list ###########################################################################
######################################################################################################################################

list1 = [5, 1, 9, 3]
list2 = [8, 2, 7, 4]

# Merge
merged = list1 + list2

# Manual sort (bubble sort example)
#take currenct and next value from list 
#compare current and next value like currenct values is greater than the next value 
#if current value is greater than the next value than swap them  
for i in range(len(merged)):
    for j in range(i + 1, len(merged)):
        if merged[i] > merged[j]:
            merged[i], merged[j] = merged[j], merged[i]

print(merged)  # Output: [1, 2, 3, 4, 5, 7, 8, 9]

################################## Flattend the list ################################################################################
######################################################################################################################################

def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if type(item) == list:
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

print(flatten([1, [2, [3, 4], 5], 6]))  # [1, 2, 3, 4, 5, 6]

################################## Check number is Amstrong or not ####################################################################
######################################################################################################################################
n = int(input("Enter the number"))
i = n
count =0
#count the number of digits
while(i>0):
	i = i//10
	count = count + 1
print(count)

i = n
sum =0
while(i>0):
	digit = i%10
	x = 1
	pro = 1
	#power calculate
	while(x <=count):
		pro = pro * digit
		x = x + 1
	sum = sum + pro
	i = i//10

if(sum == n):
	print("Amstrong number")
else:
	print("Not amstrong number")