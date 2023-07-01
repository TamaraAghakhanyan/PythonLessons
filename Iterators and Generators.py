# Iterator - iterator is an object which allows a programmer to go through
#            all the elements of a collection, a sequence, regardless of its
#            specific implementation.

# iter() -   this function takes the iterable object as an argument and return it
#            as an iterator.

# myList = [1, 2, 3, 4, 5, 6, 7]
# for element in myList:
#     print(element)
#
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# my_iter = iter(myList)
# type(my_iter)
# <
#
# class 'list_iterator'>

# next(my_iter)
# 1
# next(my_iter)
# 2
# next(my_iter)
# 3
# next(my_iter)
# 4
# next(my_iter)
# 5
# next(my_iter)
# 6
# next(my_iter)
# 7
# next(my_iter)
# Traceback (most recent call last):
#   File "/Applications/PyCharm CE.app/Contents/plugins/python-ce/helpers/pydev/pydevconsole.py", line 364, in runcode
#     coro = func()
#   File "<input>", line 1, in <module>
# StopIteration


#Generator - a special routine that can be used to control the iteration
#            behavior of a loop similar to a function a generator is defined
#            using the def key word can have parameters and it can be called
#            as opposed to a function which returns an entire array with all the values.
#            A generator function yields the values one at a time.
#            That's why it can be also called a resumable function.
#            You can traverse a sequence up to a certain point, get the result and then
#            actually suspend the execution.
#            Later, you can return to that point and resume the execution

# def my_gen(x, y):
#     for i in range(x):
#         print("i is %d" % i)
#         print("y is %d" % y)
#         yield i * y
#
#
# my_object = my_gen(10, 5)
# my_object
# < generator
# object
# my_gen
# at
# 0x10c439820 >
# type(my_object)
# <
#
# class 'generator'>
#
#
# next(my_object)
# i is 0
# y is 5
# 0
# next(my_object)
# i is 1
# y is 5
# 5
# next(my_object)
# i is 2
# y is 5
# 10
# next(my_object)
# i is 3
# y is 5
# 15
# next(my_object)
# i is 4
# y is 5
# 20
# next(my_object)
# i is 5
# y is 5
# 25
# next(my_object)
# i is 6
# y is 5
# 30
# next(my_object)
# i is 7
# y is 5
# 35
# next(my_object)
# i is 8
# y is 5
# 40
# next(my_object)
# i is 9
# y is 5
# 45
# next(my_object)
# Traceback(most
# recent
# call
# last):
# File
# "/Applications/PyCharm CE.app/Contents/plugins/python-ce/helpers/pydev/pydevconsole.py", line
# 364, in runcode
# coro = func()
# File
# "<input>", line
# 1, in < module >
# StopIteration

# Generator Expressions

# gen_exp = (x for x in range(5))
# gen_exp
# <generator object <genexpr> at 0x10c4399e0>
# type(gen_exp)
# <class 'generator'>
# next(gen_exp)
# 0
# next(gen_exp)
# 1
# next(gen_exp)
# 2
# next(gen_exp)
# 3
# next(gen_exp)
# 4
# next(gen_exp)
# Traceback (most recent call last):
#   File "/Applications/PyCharm CE.app/Contents/plugins/python-ce/helpers/pydev/pydevconsole.py", line 364, in runcode
#     coro = func()
#   File "<input>", line 1, in <module>
# StopIteration


# Itertools