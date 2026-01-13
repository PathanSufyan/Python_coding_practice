from dis import disco
from tokenize import String
from xmlrpc.client import Boolean

from pyspark.sql.streaming.stateful_processor import ListState

# sufyan practice code

print("Hello Sufyan what are you doing brother")

# Varibles
# No need to declare the var const and let
# In one name
x = 10
y = "sufyan alikhan"
# print(x + y) #TypeError: unsupported operand type(s) for +: 'int' and 'str'

print("Hello"); print("How are you?"); print("Bye bye!")
###########################################################################
###########################################################################
print("Hello World!", end=" ")
print("I will print on the same line.")

###########################################################################
############################### Print numbers ####################################
# print(3)
# print(358)
# print(50000)
#
# print(3 + 3)
# print(2 * 5)
#
# print("I am", 35, "years old.")

###########################################################################
############################### Print numbers ####################################

# s = 35
# s = "ali"
# print(s)
###########################################################################
############################### Print Casting ####################################
# x = str(3)    # x will be '3'
# y = int(3)    # y will be 3
# z = float(3)  # z will be 3.0

# print(type(x))
# print(type(y))
###########################################################################
############################### Variable declaration ####################################

# Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.

# myvar = "John"
# my_var = "John"
# _my_var = "John"
# myVar = "John"
# MYVAR = "John"
# myvar2 = "John"

# Illegal variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)

# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)

###########################################################################
############################### Global Variable declaration ####################################

# def myfunc():
#   global x
#   x = "fantastic"
# myfunc()
# print("Python is " + x)


# Built-in Data Types
# In programming, data type is an important concept.
# Variables can store data of different types, and different types can do different things.
# Python has the following data types built-in by default, in these categories:

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

# obj = {"name": "Sufyan", "age":35, "name":"khan"}
# print(obj["name"])

###########################################################
############# String ##################################
# String work like an Array, and we can loop over the Array

# aa = "sufyan"
# print(aa[0])
#
# for x in aa:
#     print(x)

ss = "PathanSufyan"
print(ss[0:3])
print("Slice start and end", ss[2:5])
print("onlyEnd", ss[:5])
print("onlystart", ss[1:])
print("negative", ss[-3:-1])

