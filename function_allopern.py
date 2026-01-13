
############################################# Function in python
# 1 Creating function
# 2 Calling the function
# 3 Arguments
# 4 Parameters
# 5 Arbitary arguments (*arguments)
# 6 Arbitrary Keyword Arguments, **kwargs
# 7 Default Parameter Value
# 8 Passing a List as an Argument
# 9 Return Values
# 10 The pass Statement
# 11 Positional-Only Arguments
# 12 Keyword-Only Arguments
# 13 Combine Positional-Only and Keyword-Only
# 14 Recursion
# 15 Lambda

# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

# 🧠 Why Use Functions?
# Avoid repetition – Write once, use many times.
# Organize code – Break large problems into smaller chunks.
# Easier debugging and testing.
# Improves code reusability and readability.

# Types of Functions in Python
# Built-in functions – Already provided by Python (e.g., print(), len(), type(), input())
# User-defined functions – Created by the programmer using the def keyword.
# Lambda functions – Anonymous, short functions defined using the lambda keyword.



#syntax
# def function_name(parameters(by default, single, multiple or tuple,list, dictionary)):
    # operation perform
    # Return something or not
# function_name(arguments(single, multiples)          Calling or invoking the function here an execution context is created and assign values

# In Python a function is defined using the def keyword:
def my_function():
  print("Hello from a function")

my_function() # calling the function

########################################################## Arguments
# Information can be passed into functions as arguments.

# Arguments are specified after the function name, inside the parentheses.
# You can add as many arguments as you want, just separate them with a comma.
# The following example has a function with one argument (fname).
# When the function is called, we pass along a first name, which is used inside the function to print the full name:
# Arguments are often shortened to args in Python documentations.
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

######################################################### Parameters
# The terms parameter and argument can be used for the same thing: information that are passed into a function.
# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called

#By default, a function must be called with the correct number of arguments.
# Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

# Arguments and parameters should be same otherwise it will give typeError

####################################################### Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function,
# add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
# If the number of arguments is unknown, add a * before the parameter name:
# Arbitrary Arguments are often shortened to *args in Python documentations.

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus") # The youngest child is Linus

# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")           # The youngest child is Linus

########################################################  Arbitrary Keyword Arguments, **kwargs

# If you do not know how many keyword arguments that will be passed into your function,
# add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:

# If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")        # His last name is Refsnes


######################################################## By default Parameter value

# The following example shows how to use a default parameter value.
# If we call the function without argument, it uses the default value:

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")   # I am from Sweden
my_function("India")    # I am from India
my_function()           # I am from Norway
my_function("Brazil")   # I am from Brazil

####################################################### Passing a List as an Argument

#You can send any data types of argument to a function (string, number, list, dictionary etc.),
# and it will be treated as the same data type inside the function.
# E.g. if you send a List as an argument, it will still be a List when it reaches the function:

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits) # apple banana cherry

####################################################### Return Values

# To let a function return a value, use the return statement:
def my_function(x):
  return 5 * x

print(my_function(3))       # 15
print(my_function(5))       # 25
print(my_function(9))       # 45

####################################################### The pass Statement

# function definitions cannot be empty, but if you for some reason have a function definition with no content,
# put in the pass statement to avoid getting an error.
def myfunction():
  pass

####################################################### Positional-Only Arguments

# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
# To specify that a function can have only positional arguments, add , / after the arguments:
# Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:

def my_function(x, /):
  print(x)

my_function(3)

###################################################### Keyword-Only Arguments

# To specify that a function can have only keyword arguments, add *, before the arguments:
def my_function(*, x):
  print(x)

my_function(x = 3)

# Without the *, you are allowed to use positional arguments even if the function expects keyword arguments:
def my_function(x):
  print(x)

my_function(3)

# But with the *, you will get an error if you try to send a positional argument:

#####################################################  Combine Positional-Only and Keyword-Only

# You can combine the two argument types in the same function.
# Any argument before the / , are positional-only, and any argument after the *, are keyword-only.

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

#####################################################   Recursion

# Recursion is a programming technique where a function calls itself to solve a smaller version of a problem until it reaches
# a base case (a stopping condition).
# In Python, recursion is a powerful method for solving problems that can be broken down into similar sub-problems, such as:
# Calculating factorial
# Fibonacci numbers
# Tree traversal
# Nested data processing

# Key Concepts of Recursion
# 1. Recursive Case
# The part of the function where it calls itself to continue the problem-solving process.
# 2. Base Case
# The condition where the function stops calling itself and starts returning values.

# General Structure of a Recursive Function
# def recursive_function(parameters):
#   if base_case_condition:
#     return result
#   else:
#     return recursive_function(smaller_problem)


def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)
# output 1 3 6 10 15 21

def fact(val):
  if val == 1:
    return  1
  else:
    return val * fact(val-1)

facts = fact(6)
print("factorial of given number",facts)

# sum of list using recursion
def sum_list(lst):
  if not lst:
    return 0
  return lst[0] + sum_list(lst[1:])

print(sum_list([1, 2, 3, 4]))  # Output: 10

# 📁 Directory/File Traversal (Conceptual)
# Used to process nested directories/files (recursively walk through folders).
import os

def traverse_directory(path):
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            traverse_directory(full_path)
        else:
            print(full_path)

# Example usage (be cautious with large paths)
# traverse_directory("/your/folder/path")

# 🔁 Reverse a String
def reverse_string(s):
  if len(s) <= 1:
    return s
  return reverse_string(s[1:]) + s[0]


print(reverse_string("hello"))  # Output: "olleh"

# 🧠 Recursion vs Loop
# | Feature      | Recursion                              | Loop                        |
# | ------------ | -------------------------------------- | --------------------------- |
# | Memory usage | Uses stack (can cause overflow)        | Efficient, uses less memory |
# | Readability  | More readable for nested/complex tasks | Better for simple tasks     |
# | Speed        | Slower due to overhead                 | Faster in most cases        |

# ⚠️ Important Notes
# Python has a recursion depth limit (sys.getrecursionlimit()), usually 1000 by default.
# You can change it with sys.setrecursionlimit(), but use caution to avoid stack overflow errors.


####################################################### Lambda function in python


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# A lambda function in Python is a small anonymous function defined using the lambda keyword.
# Unlike regular functions defined with def, a lambda function doesn't have a name and is usually used for short,
# throwaway functions.

# 🧠 Syntax
# lambda arguments: expression
# Can have any number of arguments.
# Must have only one expression (no statements like loops, if, etc.).
# Returns the value of the expression automatically (no return needed).


x = lambda a: a + 10
print(x(5))

# Add numbers
add = lambda x,y: x+y
print(add(10,20))

# square of number
sqr = lambda x : x * x
print(sqr(5))

# Check even or odd
eve_odd = lambda x: x%2==0
print(eve_odd(7))

# 📦 Where Are Lambda Functions Commonly Used?
# 1. With map()
nums = [1, 2, 3, 4]
square = list(map(lambda x : x**2, nums))
print(square)

# 2. With filter()
even = list(filter(lambda x : x%2 ==0, nums))
print(even)

# 3. With sorted() and key
people = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]
# sort by age
sorted_people = sorted(people, key=lambda person: person[1])
print(sorted_people)

#Let’s break this down:
# sorted() is a built-in Python function that returns a new sorted list (it doesn't change the original list).
# key= tells Python how to sort the list.
# lambda person: person[1] is an anonymous function that takes each person (which is a tuple like ("Alice", 25))
# and returns the second element (person[1], which is the age).


# ❗ Limitations of Lambda Functions
# | Limitation          | Description                        |
# | ------------------- | ---------------------------------- |
# | Only one expression | Cannot contain multiple statements |
# | No name (anonymous) | Hard to debug or reuse             |
# | Limited readability | Not ideal for complex logic        |

# ✅ When to Use Lambda Functions
# Use them when:
# The function is simple.
# You only need it once (e.g., in map, filter, sorted).
# You want more concise code.

