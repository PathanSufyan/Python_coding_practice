
######################## Type casting ###################################

# | **From \ To** | `int()`                 | `float()`          | `str()` | `bool()` | `list()`      | `tuple()` | `set()` | `dict()`                                            |
# | ------------- | ----------------------- | ------------------ | ------- | -------- | ------------- | --------- | ------- | --------------------------------------------------- |
# | **int**       | ✅                       | ✅                  | ✅       | ✅        | ❌             | ❌         | ❌       | ❌                                                   |
# | **float**     | ✅                       | ✅                  | ✅       | ✅        | ❌             | ❌         | ❌       | ❌                                                   |
# | **str**       | ✅ (only if numeric)     | ✅ (if valid float) | ✅       | ✅        | ✅ (as chars)  | ✅         | ✅       | ✅ (if string is valid `{"key": value}` or iterable) |
# | **bool**      | ✅                       | ✅                  | ✅       | ✅        | ❌             | ❌         | ❌       | ❌                                                   |
# | **list**      | ❌ (if elements not int) | ❌                  | ✅       | ✅        | ✅             | ✅         | ✅       | ✅ (only if list of pairs)                           |
# | **tuple**     | ❌                       | ❌                  | ✅       | ✅        | ✅             | ✅         | ✅       | ✅ (if valid pairs)                                  |
# | **set**       | ❌                       | ❌                  | ✅       | ✅        | ✅             | ✅         | ✅       | ✅ (if set of pairs)                                 |
# | **dict**      | ❌                       | ❌                  | ✅       | ✅        | ✅ (keys only) | ✅         | ✅       | ✅                                                   |



x = "sufyan"
y = 10
z = ["Pathan", "Sufyan", "ali", "khan"]
a = {
    "name": "sufyan",
    "age": 17,
    "address": {
        "area": "Paltan",
        "Phone": 7020
    }
}

# print(x)
# l = list(x)
# print(l)
# print(type(l))
# print(len(l))

############################################## String ##########################################################


a = "Hello world"
print(a)
# print(a[1])
# print(len(a))

# for i in a:
#     print(i)

# print("Hello" in a)
# print("Hello" not in a)

# if "Hello" in a:
#     print("present in", a)
# else:
#     print("Not in")

###################################### Slicing in the String ############################################
# [Start:End:Increment]
# print(a[0:5])
# print(a[:])
# print(a[0:])
# print(a[:5])
# print(a[-4:-1])
# print(a[-4:])
# print(a[:-1])

###################################### Modify the String ##################################################
# print("1",a.upper())
# print("2",a.lower())
# print("3",a.title())            #first Character of each work capital
# print("4",a.capitalize())       #only capital first alphabet
# print("5",a.strip())            #remove space before and after
# print("6",a.replace("H", "w"))
# print("7",a.split(" "))         #seperate and convert String to list
# print("8",a.split(","))
# print("9",list(a))                  #['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
# print("10", [char for char in a])   #['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
# print("11", [*a])                   #['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']


##############################################  Concatenation in String #########################################
# b = "Sufyan"
# c = "alikhan"
# d = 10
# print(b+" "+c)
# print(c+d)                      #TypeError: can only concatenate str (not "int") to str
# print(f"My name is {b}")          #Format the String

##############################################  String Methods ###############################################
# b = "Sufyan"
# c = "alikhan"
# d = 10

############ Insert
# print(b+c)                      #concatination
# print(f"My age is {d}")         #formating the string

########### Update
# print(a.replace("Hello", "wello"))

# Delete (select perticular word slice it and make new from it)

########### Convert to another data type
# using typecasting
# my_list = ["Hello", "world", "!"]
# print(a.split())                #Convert String to list
# print(" ".join(my_list))        #Convert list to String


############ Reverse
# print(" ".join(reversed(a)))
# print(a[::-1])

############ Finding or searching something in the string
# if "Hello" in a:
#     print("Present")

# print([char for char in a])
# print(a.find("l"))                  #string.find(value, start, end),first occurrence of the specified values index number.returns -1 if the value is not found.
# print((a.index("l")))               #string.index(value, start, end) same as find except it gives an error if value is not find

############ Counting characters/words in the string
# print(a.count("l"))               #string.count(value, start, end)

############ Loop over the string
print(a)
# print([char for char in a])

# for i in a:
#     print(i)

# for i in range(len(a)):
#     print(i,a[i])

# for index, character in enumerate(a):
#     print(index, character)

# i=0
# while i<len(a):
#     print(a[i])
#     i +=1

# 1 number of occurence of character or word
# 2 vowels in the string or list


import time
start = time.time()
for i in range(1, 101):
    print(i)

print(time.time()-start)