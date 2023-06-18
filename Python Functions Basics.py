def my_first_function():
    "This is our first function!"
    print("Hello World")

my_first_function()

def my_first_function():
    "This is our first function!"
    print("Hello Java")

my_first_function()

def my_second_function(x, y):
    print("Hello " + x)
    print("Hello " + y)

my_second_function("Python", "Java")

def my_sum(x,y):
    sum = x + y
    return sum

print(my_sum(1,3))

def my_sum(x,y,z):
    sum = (x + y) * z
    return sum ** 2

print(my_sum(1,2,3))


# Types of Arguments:

# 1. Positional arguments: Argument count and positions should be the same

# def my_sum(x,y,z):
#     sum = (x + y) * z
#     return sum ** 2
#
# print(my_sum(1,2,))
#
# Traceback (most recent call last):
#   File "/Users/tamaraaghakhanyan/MyPythonLessons/lessons/python/lessons/Python Functions Basics.py", line 39, in <module>
#     print(my_sum(1,2,))
# TypeError: my_sum() missing 1 required positional argument: 'z'


# 2. Keyword arguments: we can ignore the order pf the arguments we enter or
# skip some of them

print(my_sum(x = 1, y = 2, z = 3))

print(my_sum(z = 3, y = 2, x = 1))

# print(my_sum(x = 1, y = 2, 3))
# SyntaxError: positional argument follows keyword argument:
print(my_sum(1, 2, z = 3))

print(my_sum(10, 20, z = 3))

# 3. Define  a default value for an argument:

def my_sum(x,y,z = 3):
    sum = (x + y) * z
    return sum ** 2

print(my_sum(1,2))

# if we want to use another argument for the default value we should
# specify it in function:

def my_sum(x,y,z = 3):
    sum = (x + y) * z
    return sum ** 2

print(my_sum(1,2,4))

# to specify a variable number of parameters in the function:

# for positional arguments:
def function1(x,*args):  #*args - potential count of arguments, it is an empty tuple
    print("hello")

print(function1("hello"))
def function1(x,*args):
    print("hello")
    print(args)

print(function1("hello"))

def function1(x,*args):
    print(x)
    for argument in args:
        print(argument)

print(function1("hello", 1, 2, 3))




# for keyword arguments:

def function1(x,**kwargs):
    print(x)
    for argument in kwargs:
        print(argument)


