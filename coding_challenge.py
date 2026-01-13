# We have a number 1004,
# If number contain 0 then replace it with 5
# Question 1004, answer is 1554

# num = 1004
# num3 = str(num)
#
# num4 = ' '.join(num3)
# print(num4)
# num5 = num4.split(' ')
# print(num5)
#
#
# num6 = list(num3)
# print("num6",num6)

# for char in num6:
#     if char == '0':
#         char = 5
#     else:
#         print(char)
#

# def converter(para):
#     li = []
#     if len(para) == 0:
#         return
#     for char in para:
#         if char ==0:
#             char = 5
#             li.append(char)
#         else:
#             li.append(char)
#
#     return li
#
# lii = [1,0,0,4]
# print(lii)
# val = converter(lii)
# print(val)

# Question 2: Given an integer n, your task is to compute the sum of all natural numbers from 1 to n. if n is 0
# then sum should be zero
#
# conditions
# n=1 then return 1
# n=0 then return 0
# n = any thing then sum all the values

# n=4
# sum = 0
# while n>0:
#     sum = sum + n
#     n=n-1
#
# print(sum)

# def sum(para):
#     sumval = 0
#     if para == 0:
#         return 0
#     if para == 1:
#         return 1
#     while para > 0:
#         sumval = sumval + para
#         para = para - 1
#     return sumval
#
# val = sum(5)
# print(val)

num = 5
sum = 0
for i in range(1,num+1):
    sum = sum + i

print(sum)