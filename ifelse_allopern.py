# Python Conditions and If statements
# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# These conditions can be used in several ways, most commonly in "if statements" and loops.

# An "if statement" is written by using the if keyword.

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
# In this example a is equal to b, so the first condition is not true, but the elif condition is true,
# so we print to screen that "a and b are equal".

# The else keyword catches anything which isn't caught by the preceding conditions.
# In this example a is greater than b, so the first condition is not true,
# also the elif condition is not true, so we go to the else condition and print to screen that "a is greater than b".
# You can also have an else without the elif:

# If you have only one statement to execute, you can put it on the same line as the if statement.
if a > b: print("a is greater than b")

# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
print("A") if a > b else print("B")

# This technique is known as Ternary Operators, or Conditional Expressions.
# You can also have multiple else statements on the same line:
print("A") if a > b else print("=") if a == b else print("B")

# The and keyword is a logical operator, and is used to combine conditional statements:
# Test if a is greater than b, AND if c is greater than a:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# The or keyword is a logical operator, and is used to combine conditional statements:
# Test if a is greater than b, OR if a is greater than c:
if a > b or a > c:
  print("At least one of the conditions is True")


# The not keyword is a logical operator, and is used to reverse the result of the conditional statement:
# Test if a is NOT greater than b:
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

# You can have if statements inside if statements, this is called nested if statements.
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# pass acts as a placeholder when no action is needed.
x = 5
if x > 0:
    pass  # Do nothing for now
else:
    print("x is not positive")

#  if in List Comprehensions (Advanced)
nums = [1, 2, 3, 4, 5]
even = [x for x in nums if x % 2 == 0]

# Match-Case (Python 3.10+) – Alternative to if-elif-else
status = 404

match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case _:
        print("Unknown status")


