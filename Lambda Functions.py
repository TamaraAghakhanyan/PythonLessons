# Syntax for Lamda functions:
# lambda arg1, arg2, ..., arg n: in anexpressions using the arguments

# a = lambda x, y: x * y
# a
# <function <lambda> at 0x101ad98b0>
# type(a)
# <class 'function'>
# a(2,10)
# 20
# a(5, 50)
# 250

# Classic way:
# def myfunc(mylist):
#     list_xy = []
#     for x in range(10):
#         for y in range(5):
#             result = x * y
#             list_xy.append(result)
#     return list_xy + mylist

# myfunc([100, 101, 102])
# [0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 0, 2, 4, 6, 8, 0, 3, 6, 9,
# 12, 0, 4, 8, 12, 16, 0, 5, 10, 15, 20, 0, 6, 12, 18, 24, 0,
# 7, 14, 21, 28, 0, 8, 16, 24, 32, 0, 9, 18, 27, 36, 100, 101, 102]

# writing the above block of code using lamda function and list comprehension:

# b = lambda mylist: [ x * y for x in range(10) for y in range(5)] + mylist
# b([100,101, 102])
# [0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 0, 2, 4, 6, 8, 0, 3, 6, 9,
# 12, 0, 4, 8, 12, 16, 0, 5, 10, 15, 20, 0, 6, 12, 18, 24, 0,
# 7, 14, 21, 28, 0, 8, 16, 24, 32, 0, 9, 18, 27, 36, 100, 101, 102]


# map() & filter()


# map() - takes a function and the sequence as arguments and applies the
#         function to all the elements of the sequence returning on iterable
#         object. As the result, the function taken as the first argument
#         may be a previously defined function or a lamda function.

# def product10(a):
#     return a * 10
#
# r1 = range(10)
# map(product10,r1)
# <map object at 0x10c53c520>
# list(map(product10,r1))
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

# the same with lambda function:


# map((lambda a: a * 10), r1)
# <map object at 0x10c53c1c0>
# list(map((lambda a: a * 10), r1))
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]


# filter() - takes a function and the sequence as arguments, and its
#            role is to extract all the elements in the sequence for
#            which the function returns True.

# list(filter((lambda a: a > 5), r1))
# [6, 7, 8, 9]