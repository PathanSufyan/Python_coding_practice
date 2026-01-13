



# 🔁 Set vs Other Data Structures
# | Feature           | Set             | List               | Tuple            | Dictionary         |
# | ----------------- | -------------   | ------------------ | ---------------- | ------------------ |
# | Ordered           | ❌ (Py 3.6+ ✅) | ✅                  | ✅              | ✅               |
# | Mutable           | ✅              | ✅                  | ❌              | ✅                |
# | Allows Duplicates | ❌              | ✅                  | ✅              | Keys ❌, Values ✅ |
# | Indexed           | ❌              | ✅                  | ✅              | Keys only        |
# | Syntax            | `{1, 2, 3}`    | `[1, 2, 3]`        | `(1, 2, 3)`      | `{'a': 1, 'b': 2}` |
# | Use Case          | Unique items   | Ordered collection | Immutable record | Key-value pairs    |



# When to use
# | Situation                                | Use Set?             |
# | ---------------------------------------- | -------------------- |
# | Need to eliminate duplicates             | ✅ Yes                |
# | Need to do union/intersection/difference | ✅ Yes                |
# | Need indexing or ordering                | ❌ No, use list/tuple |
# | Need fast membership testing             | ✅ Yes                |



# 🧠 Important Notes
# Empty {} is a dictionary, not a set — use set() for an empty set.
# Set elements must be hashable — so no lists or dictionaries inside sets.
# Use frozenset for an immutable version of set.


# Pros and cons
# | Advantage                            | Explanation                                          |
# | ------------------------------------ | ---------------------------------------------------- |
# | **No duplicates**                    | Ensures uniqueness automatically.                    |
# | **Fast membership testing**          | `in` operator is faster than in lists.               |
# | **Supports mathematical operations** | Useful for data analysis, filters, comparisons.      |
# | **Memory efficient**                 | More optimized than lists when storing unique items. |

# | Limitation                             | Explanation                                          |
# | -------------------------------------- | ---------------------------------------------------- |
# | **Unordered**                          | No index-based access.                               |
# | **No duplicates allowed**              | May not be useful if you need repeated items.        |
# | **Mutable but only hashable elements** | Cannot contain unhashable types like lists or dicts. |
# | **No slicing or indexing**             | Unlike lists or tuples.                              |




# Common Set Operations
# | Operation              | Syntax / Example                        |                      |
# | ---------------------- | --------------------------------------- | -------------------- |
# | Add element            | `s.add(x)`                              |                      |
# | Remove element         | `s.remove(x)` or `s.discard(x)`         |                      |
# | Union                  | \`s1                                    | s2`or`s1.union(s2)\` |
# | Intersection           | `s1 & s2` or `s1.intersection(s2)`      |                      |
# | Difference             | `s1 - s2` or `s1.difference(s2)`        |                      |
# | Symmetric Difference   | `s1 ^ s2`                               |                      |
# | Subset / Superset Test | `s1.issubset(s2)` / `s1.issuperset(s2)` |                      |
# | Clear All              | `s.clear()`                             |                      |
# | Copy                   | `s.copy()`                              |                      |


######################################################### 1 Create
my_set = {1, 2, 3}
empty_set = set()  # Important: {} creates a dict, not a set

########################################################## 2 Add

my_set.add(4)  # Adds 4 to the set

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)



########################################################## 3 Update

my_set.update([5, 6, 7])  # Adds multiple values

########################################################## 4 Delete

my_set.remove(2)    # Removes 2; raises KeyError if not found
my_set.discard(3)   # Removes 3; does NOT raise an error if not found
my_set.clear()      # Empties the set
x = thisset.pop()
del thisset

########################################################## 5 Copy

original = {1, 2, 3}
copy_set = original.copy()

########################################################## 6 Sort (Farward, Reverse)

s = {4, 1, 3, 2}
sorted_forward = sorted(s)            # [1, 2, 3, 4]
sorted_reverse = sorted(s, reverse=True)  # [4, 3, 2, 1]

########################################################## 7 Looping over it

for item in my_set:
    print(item)

########################################################## 8 Accessing element
# ❌ Sets do not support indexing.

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

print("banana" in thisset)

print("banana" not in thisset)

s = {10, 20, 30}
for i, val in enumerate(s):
    if i == 1:
        print("Second item:", val)
        break


########################################################## 9 Highest and lowest value

s = {5, 1, 9, 2}
print("Max:", max(s))
print("Min:", min(s))

########################################################## 10 Merging two

# Join Sets
# There are several ways to join two or more sets in Python.
# The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the duplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
set3 = set1 | set2
print(set3)

set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
myset = set1 | set2 | set3 |set4
print(myset)

set1.update(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
set3 = set1 & set2
print(set3)         # {'apple'}


set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", "microsoft", "apple", True}
set3 = set1.intersection(set2)
print(set3)         # {False, True, 'apple'}

set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
set3 = set1 - set2
print(set3)         # {'banana', 'cherry'}

set3 = set1.symmetric_difference(set2)
print(set3)         # {'google', 'banana', 'microsoft', 'cherry'}


s1 = {1, 2, 3}
s2 = {3, 4, 5}
merged = s1.union(s2)  # or s1 | s2


########################################################## 11 Convert to other data types

s = {1, 2, 3}

# To list
as_list = list(s)

# To tuple
as_tuple = tuple(s)

# To string
as_string = str(s)

########################################################## 12 Searching

print(2 in s)  # True if 2 exists in the set

########################################################## 13 Comparing

a = {1, 2, 3}
b = {1, 2, 3, 4}

print(a == b)            # False
print(a.issubset(b))     # True
print(b.issuperset(a))   # True

########################################################## 14 Removing duplicates

dup_list = [1, 2, 2, 3, 3, 3]
unique_set = set(dup_list)  # {1, 2, 3}


# Method	Shortcut	Description
# add()	 	                    Adds an element to the set
# clear()	 	                    Removes all the elements from the set
# copy()	 	                    Returns a copy of the set
# difference()	-	            Returns a set containing the difference between two or more sets
# difference_update()	-=	        Removes the items in this set that are also included in another, specified set
# discard()	 	                Remove the specified item
# intersection()	&	            Returns a set, that is the intersection of two other sets
# intersection_update()	&=	    Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	 	            Returns whether two sets have a intersection or not
# issubset()	<=	                Returns whether another set contains this set or not
#  	<	                        Returns whether all items in this set is present in other, specified set(s)
# issuperset()	>=	            Returns whether this set contains another set or not
#  	>	                        Returns whether all items in other, specified set(s) is present in this set
# pop()	 	                    Removes an element from the set
# remove()	 	                Removes the specified element
# symmetric_difference()	^	    Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
# union()	|	                    Return a set containing the union of sets
# update()	|=	                Update the set with the union of this set and others


