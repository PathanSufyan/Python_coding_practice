# Type casting in Python means converting one data type into another. Python supports **implicit** and **explicit** type casting.
#
# ---
#
# ## ✅ **What We Can Do in Type Casting**
#
# ### 🔹 **Implicit Type Casting** (Done by Python automatically)
#
# Python automatically converts one data type to another when it's safe.
#
# ```python
# x = 10       # int
# y = 2.5      # float
#
# result = x + y
# print(result)        # 12.5 (float)
# print(type(result))  # <class 'float'>
# ```
#
# ---
#
# ### 🔹 **Explicit Type Casting** (You convert it manually)
#
# You can use functions like:
#
# * `int()`
# * `float()`
# * `str()`
# * `bool()`
# * `list()`
# * `tuple()`
# * `set()`
# * `dict()` *(with correct format only)*
#
# #### Examples:
#
# ```python
# # int to float
# a = 10
# print(float(a))  # 10.0
#
# # float to int
# b = 5.9
# print(int(b))    # 5 (truncates the decimal)
#
# # int to string
# c = 123
# print(str(c))    # '123'
#
# # string to int (if it's numeric)
# d = "456"
# print(int(d))    # 456
#
# # list to set
# lst = [1, 2, 2, 3]
# print(set(lst))  # {1, 2, 3}
# ```
#
# ---
#
# ## ❌ **What We Cannot Do or Will Cause Errors**
#
# ### 🔸 **Invalid conversions that will raise errors**
#
# #### 1. Non-numeric strings to numbers
#
# ```python
# x = "hello"
# int(x)        # ❌ ValueError
# ```
#
# #### 2. Converting complex numbers to int or float
#
# ```python
# z = 3 + 4j
# int(z)        # ❌ TypeError
# ```
#
# #### 3. Converting dictionary to list of keys is okay, but to `int`, `str` directly can fail
#
# ```python
# d = {'a': 1, 'b': 2}
# list(d)       # ✅ ['a', 'b']
# int(d)        # ❌ TypeError
# ```
#
# #### 4. String list to int list (directly)
#
# ```python
# lst = ['1', '2', '3']
# int(lst[0])   # ✅ 1
# int(lst)      # ❌ TypeError
# ```
#
# ---
#
# ## 🔍 Summary Table
#
# | Conversion              | Allowed? | Example                     |
# | ----------------------- | -------- | --------------------------- |
# | int ➡ float             | ✅        | `float(5)` → `5.0`          |
# | float ➡ int             | ✅        | `int(7.8)` → `7`            |
# | str (numeric) ➡ int     | ✅        | `int("123")` → `123`        |
# | str (non-numeric) ➡ int | ❌        | `int("abc")` → `ValueError` |
# | complex ➡ int/float     | ❌        | `int(3+4j)` → `TypeError`   |
# | list ➡ set              | ✅        | `set([1, 2, 2])` → `{1, 2}` |
# | list ➡ int              | ❌        | `int([1, 2])` → `TypeError` |
#
# ---
#
# Let me know if you want a cheat sheet or small project-based examples to practice type casting.

################################################ Numbers ###############################################
# In Python, numbers are fundamental data types, and Python provides **powerful capabilities** for working with them. However, there are also **limits and restrictions**.
#
# ---
#
# ## ✅ **What We Can Do with Numbers in Python**
#
# ### 🔹 1. **Arithmetic Operations**
#
# You can use all standard arithmetic operators:
#
# ```python
# a = 10
# b = 3
#
# print(a + b)   # 13
# print(a - b)   # 7
# print(a * b)   # 30
# print(a / b)   # 3.333...
# print(a // b)  # 3 (floor division)
# print(a % b)   # 1 (modulus)
# print(a ** b)  # 1000 (exponentiation)
# ```
#
# ---
#
# ### 🔹 2. **Comparison Operators**
#
# Used for conditions and logical flows.
#
# ```python
# a = 5
# b = 10
#
# print(a == b)  # False
# print(a < b)   # True
# ```
#
# ---
#
# ### 🔹 3. **Type Conversion**
#
# ```python
# int(5.6)      # 5
# float(3)      # 3.0
# str(10)       # '10'
# complex(2)    # (2+0j)
# ```
#
# ---
#
# ### 🔹 4. **Math Functions** (using the `math` module)
#
# ```python
# import math
#
# math.sqrt(25)      # 5.0
# math.pow(2, 3)     # 8.0
# math.factorial(5)  # 120
# math.floor(5.9)    # 5
# math.ceil(5.1)     # 6
# ```
#
# ---
#
# ### 🔹 5. **Random Numbers** (via `random` module)
#
# ```python
# import random
#
# random.randint(1, 100)   # Random int between 1 and 100
# random.random()          # Random float between 0 and 1
# ```
#
# ---
#
# ### 🔹 6. **Bitwise Operations**
#
# ```python
# print(5 & 3)   # 1
# print(5 | 3)   # 7
# print(5 ^ 3)   # 6
# print(~5)      # -6
# ```
#
# ---
#
# ### 🔹 7. **Use in Loops and Conditions**
#
# ```python
# for i in range(5):   # Loops from 0 to 4
#     print(i)
# ```
#
# ---
#
# ## ❌ **What We Cannot Do with Numbers in Python**
#
# ### 🔸 1. **Concatenation with Strings Without Casting**
#
# ```python
# age = 25
# print("Age is " + age)  # ❌ TypeError
# # ✅ Correct way:
# print("Age is " + str(age))
# ```
#
# ---
#
# ### 🔸 2. **Division by Zero**
#
# ```python
# x = 10
# y = 0
# # print(x / y)  # ❌ ZeroDivisionError
# ```
#
# ---
#
# ### 🔸 3. **Using Methods Like `.append()` or `.upper()`**
#
# Numbers are not collections or strings:
#
# ```python
# num = 10
# # num.append(5)    # ❌ AttributeError
# # num.upper()      # ❌ AttributeError
# ```
#
# ---
#
# ### 🔸 4. **Changing Value of Immutable Number Object in Place**
#
# ```python
# a = 10
# b = a
# a += 1
# print(b)  # 10, not 11 → because integers are immutable
# ```
#
# ---
#
# ### 🔸 5. **Very Large or Complex Mathematical Computations Without Limits**
#
# Python supports big integers, but:
#
# * Extremely large floats can cause **overflow**
# * Too deep recursion or complex math can cause **crash or slowdown**
#
# ```python
# import math
# math.exp(1000)  # ❌ OverflowError
# ```
#
# ---
#
# ## 🧠 Summary Table
#
# | Operation                    | Possible? | Notes                               |
# | ---------------------------- | --------- | ----------------------------------- |
# | Arithmetic (+, -, \*, /)     | ✅         | Fully supported                     |
# | Type casting (int, float)    | ✅         | With valid input                    |
# | Division by 0                | ❌         | Causes ZeroDivisionError            |
# | String + Number              | ❌         | Must convert number to string first |
# | Use `.append()` on number    | ❌         | Not allowed, numbers are not lists  |
# | Exponential math (e.g., pow) | ✅         | Supported via `**` or `math` module |
# | Use in loops/conditions      | ✅         | Works great                         |
#
# ---
#
# Let me know if you want practice problems or real-world examples using numbers in Python (e.g., billing, loan calculation, tax calculation).



####################################### String ##################################
