from traceback import print_tb


# Class in python
# Attribute means variables
# Instance mean Object

# A class is a blueprint for creating objects.
# An object is an instance of a class.
#

# Class ye ek blue print hai jis se objects banate hai

# Always use capital start character of class name
# Class takes argument
# If we takes the argument then to handle it we have a function
# __init__ special function name or constructor function it calls immediately when class object is created
# Object bante time constructor call hota hai
# self is reference of argument/ parameters of which object

# 1 Class class_name
# 2 function def __init__(self):
# 3 self


###############################################################################################################################
##############################################################################################################################
# simple Classes
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
# my_car = Car("Toyota", "Corollela")  # Here we are creating an object from the class
# print(my_car)
# print(my_car.brand)
# print(my_car.model)

###############################################################################################################################
##############################################################################################################################
# We can add the methods or more functionality to class

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def full_name(self):
#         return f"{self.brand} {self.model}"
#
# my_car = Car("Toyota","Carolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

###############################################################################################################################
#########################################  Inheritance   ##############################################################
# we can also inherit the other class functionality to avoid unnecessary write more code
# Inheritance

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def full_name(self):
#         return f"{self.brand} {self.model}"
#
#
# class ElectricCar(Car):
#     def __init__(self,brand, model,battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size
#
#
# # my_car = Car("Toyota","carolla")
# # print(my_car.full_name())
#
# my_second_car = ElectricCar("Tesla", "S2", "80kwh")
# print(my_second_car.battery_size)


###############################################################################################################################
###############################################   Encapsulation  ###########################################################
# Private variable

# we can hide some variables(attribute), so that from outside the class we cannot access through its object
# Encapsulation
# Here we hide the brand variable or attribute
# through a function we can access that brand to its object using a getter function
# It is not mandatory to write the getter before the function name we can use anything in the name
# add __ before the variable

# create the class like class Car:
# It has functions which takes arguments and immediately call like def __init__(self):
# inside this function we pass the parameters like def __init__(self, brand, model):
# Now create the variables inside that function self.brand = brand
# we can also create the another functions inside the class def full_name(self):
# Every function inside the class takes self as a parameter

# class Car:
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.model = model
#
#     def full_name(self):
#         return f"{self.__brand} {self.model}"
#
#     def get_brand_access_outside(self):
#         return self.__brand
#
# Encapsulated method
#       def __is_valid_amount(self, amount):
#            return amount > 0

# class ElectricCar(Car):
#     def __init__(self,brand,model,battery_size):
#         super().__init__(brand,model)
#         self.battery_size = battery_size
#
#
# my_xuv = ElectricCar("Tesla","S2","80kwh")
# print(my_xuv.model)
# # print(my_xuv.brand)
# print(my_xuv.get_brand_access_outside())
# print(my_xuv.battery_size)

# We can only access the private variable within that class only if you want to access that variable from outside of the class
# or inside its object then we have to create a function which return that variable so that we can access it from outside

###############################################################################################################################
#####################################    Polymorphism   ##################################################################
# Many forms
# Same function name behaves differently for different classes.
# Different classes with same name function
# Same fuel type function in both the classes

# class Car:
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.model = model
#
#     def funll_name(self):
#         return  f"{self.__brand}{self.model}"
#
#     def get_access_privat(self):
#         return self.__brand
#
#     def fuel_type(self):
#         return "fuel type is Petrol"
#
# class ElectricCar(Car):
#     def __init__(self, battery_size, brand, model):
#         super().__init__(brand, model)
#         self.battery_size = battery_size
#
#     def fuel_type(self):
#         return "Fuel type Electric charge"
#
#
# my_car = Car("Tata","corolla")
# # print(my_car.model)
# # print(my_car.get_access_privat())
# print(my_car.fuel_type())
#
# my_secondcar = ElectricCar("40Khz","Tesla","S2")
# print(my_secondcar.model)
# print(my_secondcar.get_access_privat())
# print(my_secondcar.fuel_type())


###########################################################################################################################
############################################

# Class se kitne objects ban rahe hai batao

# class Car:
#     total_car = 0
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.model = model
#         Car.total_car +=1       #(or self.total_car +=1 aisa bhi krsakte ho)
#
#     def funll_name(self):
#         return  f"{self.__brand}{self.model}"
#
#     def get_access_privat(self):
#         return self.__brand
#
#     def fuel_type(self):
#         return "fuel type is Petrol"
#
# class ElectricCar(Car):
#     def __init__(self, battery_size, brand, model):
#         super().__init__(brand, model)
#         self.battery_size = battery_size
#
#     def fuel_type(self):
#         return "Fuel type Electric charge"
#
# my_car = Car("TATA", "safari")
# my_2car = Car("TATA", "corolla")
# my_3car = ElectricCar("85Khz","Tesla","S3")

# print(Car.total_car)                # Car class ke objects kitne bane including its inherite class objects

# If it gives wrong objects means Garbage collector are not immediately collect it

########################################################################################################################
########################################    Static Method ###########################################################

# A method that can only be access by only class not by its Objects(Instances)

# A static method is a method that belongs to a class but does not access instance (self) or class-level (cls) data.
# It behaves like a regular function, but it lives in the class’s namespace.
# In Python, it is defined using the @staticmethod decorator.
# "Static methods do not access instance data — but they can still be called by an instance."

# class Car:
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.model = model
#
#     def funll_name(self):
#         return  f"{self.__brand}{self.model}"
#
#     def get_access_privat(self):
#         return self.__brand
#
#     def fuel_type(self):
#         return "fuel type is Petrol"
#
#     @staticmethod
#     def general_description():
#         return "Cars are mean of transportation"
#
# class ElectricCar(Car):
#     def __init__(self, battery_size, brand, model):
#         super().__init__(brand, model)
#         self.battery_size = battery_size
#
#     def fuel_type(self):
#         return "Fuel type Electric charge"
#
#
#
# my_car = Car("TATA", "safari")
# print(Car.general_description())
# print(my_car.general_description())
# "Static methods do not access instance data — but they can still be called by an instance."

# here we only call the general
# | Can an object call a static method? | ✅ Yes |
# | Can a static method access self (instance)? | ❌ No |
# | Is the object passed to the static method? | ❌ No |
# | So what’s the point of using it in a class? | ✅ Organizational and logical grouping of related methods |


#######################################################################################################################
# How to make read only variables and functions which cannot modify but we can read it.

# How to check the Object or instance is created from which Class
# print(isinstance(my_car, Car))
# print(isinstance(my_car, ElectricCar))

########################################################################################################################
#############################  Multiple Inheritance
# Multiple Inheritance means a class can inherit from more than one parent class.


# class Engine:
#     def start(self):
#         return "Engine started"
#
# class Battery:
#     def charge(self):
#         return "Battery charging"
#
# # Child inherits from both Engine and Battery
# class ElectricCar(Engine, Battery):
#     pass
#
# car = ElectricCar()
# print(car.start())   # Inherited from Engine
# print(car.charge())  # Inherited from Battery


# | Use Case             | Description                                                           |
# | -------------------- | --------------------------------------------------------------------- |
# | 🧩 Code Reuse        | Combine features from multiple classes without rewriting code.        |
# | 🧠 Logical Structure | Models objects that share behaviors from different categories.        |
# | 🔧 Mixins            | Add optional behaviors to a class (e.g., `LoggerMixin`, `JSONMixin`). |


# ⚠️ Problem: Method Resolution Order (MRO)
# If two parent classes have methods with the same name, Python needs to decide which one to call.
# That’s where MRO (Method Resolution Order) comes in.

# class A:
#     def greet(self):
#         return "Hello from A"
#
# class B:
#     def greet(self):
#         return "Hello from B"
#
# class C(A, B):  # C inherits from A and B
#     pass
#
# c = C()
# print(c.greet())  # Which greet() is called?
# Hello from A
# Why? Because Python looks at the order: C(A, B) → A comes first.

# 🧠 How Python Solves It: MRO (Method Resolution Order)
# You can see the MRO with: print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

# 🧰 super() in Multiple Inheritance
# super() follows the MRO, not just the immediate parent.

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()

class C(A):
    def show(self):
        print("C")
        super().show()

class D(B, C):
    def show(self):
        print("D")
        super().show()

obj = D()
obj.show()

# output D
# B
# C
# A

# Why? Because of MRO:
# D → B → C → A

# 📐 MRO Tree and Resolution Flow
#   A
#  / \
# C   B
#  \ /
#   D

# But the MRO (linearized) is:
# D → B → C → A → object


# ✅ Q1. What is Multiple Inheritance and how is it handled in Python?
# Answer:
# It allows a class to inherit from more than one base class. Python uses MRO (Method Resolution Order)
# to resolve conflicts when methods exist in multiple parents.

# ✅ Q2. What is C3 Linearization?
# Answer:
# C3 Linearization is the algorithm Python uses to define the MRO. It creates a consistent order of method resolution
# in complex inheritance trees, ensuring that a class is always called before its parent.

# ✅ Q4. What is the role of super() in multiple inheritance?
# Answer:
# super() calls the next method in MRO, not just the immediate superclass.
# This makes sure all parent classes are used in order.

# ✅ Q5. What is a mixin and how does it relate to multiple inheritance?
# Answer:
# A mixin is a small class that adds reusable functionality. You combine it with other classes using multiple inheritance.

