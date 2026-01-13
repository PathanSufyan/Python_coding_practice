

########################################### while loop
# 1 While and for loop
# 2 Break
# 3 Continue
# 4 Else statement
# 5 Range()
# 6 Nested loop
# 7 Pass

# we can loop over the itrerables like string, list, tuple, dictionary and files


# The while loop requires relevant variables to be ready,
# in this example we need to define an indexing variable, i, which we set to 1.

# define i
# while condition:
# do operation you want to perform
# Increment or decrement of i
# Indentation is must see

i = 1
while i < 6:
  print(i)
  i += 1

# Note: remember to increment i, or else the loop will continue forever.

########################################### Break
# With the break statement we can stop the loop even if the while condition is true:
i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1
# output = 1 2 3

########################################## Continue statement
# With the continue statement we can stop the current iteration, and continue with the next:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
# # Note that number 3 is missing in the result

########################################## Else statement
# With the else statement we can run a block of code once when the condition no longer is true:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
# output 1 2 3 4 5 6 i is no longer less than 6

##############################################################################################################################
#############################################################################################################################

# for loop
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages,
# and works more like an iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# The for loop does not require an indexing variable to set beforehand.

# Even strings are iterable objects, they contain a sequence of characters:
for x in "banana":
  print(x)

#################################### Break in for loop
# With the break statement we can stop the loop before it has looped through all the items:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
# output apple banana

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
# output apple (Exit the loop when x is "banana", but this time the break comes before the print:)


###################################### Continue statement with for loop
# With the continue statement we can stop the current iteration of the loop, and continue with the next:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
# output apple cherry

###################################### Range in for loop
# syntax range(start, end, increment)
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default,
# and increments by 1 (by default), and ends at a specified number.
#
for x in range(6):
  print(x)
#output 0 1 2 3 4 5
# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by
# adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
for x in range(2, 6):
  print(x)
# output 2 3 4 5

# The range() function defaults to increment the sequence by 1,
# however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
for x in range(2, 30, 3):
  print(x)
# output 2 5 8 11 14 17 20 23 26 29

################################################ If else with for loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
#
for x in range(6):
  print(x)
else:
  print("Finally finished!")
# output 0 1 2 3 4 5 Finally finished!
# Note: The else block will NOT be executed if the loop is stopped by a break statement.

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#If the loop breaks, the else block is not executed.

############################################# Nested for loop

# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":
# If we have condition like 3 times both loops are run then for 1st outer loop inner will be run 3 times (1 outer 3 inner)
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
# output
# red apple
# red banana
# red cherry............

########################### pass

# for loops cannot be empty, but if you for some reason have a for loop with no content,
# put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass

# having an empty for loop like this, would raise an error without the pass statement



# How behind the scene loop is work
# Iterable tool ==> iter() ===> Iterable Objects (string, list, tuple, dict and files) ===> response(__next__)
#        ||                                                                                       ||
#           <=====================================================================================
# 1 Iterable tool (where to start, where stop loop, how goes to next step)
# 2 Iterable Objects (string, list, tuple,dict or files(files have there own iter tool))
# 3 response (__next___)

file_read = open("data")
file_read.readlines()

# How to find the memory location
l = [1,2,3]
print(iter(l))

file_read = open("data")
# print(file_read.readlines())
# print(file_read.readlines())

# print(file_read.__next__())
# print(file_read.__next__())
# print(file_read.__next__())

# for line in open("data"):
#     print(line, end="")

# while True:
#     line = file_read.readlines()
#     if not line: break
#     print(line, end="")

# How to find the memory location of list
l = [1,2,3]
# print(iter(l))
# location = iter(l)
# print(location.__next__())
# print(location.__next__())
# print(location.__next__())
# print(location.__next__())

# print(iter(l) is l)   # original memory reference and iterable memory reference is different hence we get the false

R = range(3)
print(R)
# x = iter(R)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))


############################################ Yield (Remember the state where it was, and return the value)

def even_generator(limit):
  for i in range(2, limit + 1 ,2):
    yield i

for num in even_generator(10):
  print(num)
