
# lexical scoping
# execution context
# Hoisting
# Scope chaining
# closures
# Single threaded or Multi threaded
#

def outer(num):
    def inner(x):
        return x ** num
    return inner

# f = outer(2)(3)
# print(f(3))
# print(f)
