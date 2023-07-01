# List Comprehensions
#
# list1 = []
# for i in range(10):
#     result = i ** 2
#     list1.append(result)

# list1
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# or we can write above block of code in one line by using List Comprehension:

# list2 = [x ** 2 for x in range(10)]
# list2
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# to add conditional statement to this looping construct:

# list3 = [x ** 2 for x in range(10) if x > 5]
# list3
# [36, 49, 64, 81]


# Set Comprehensions
# set1 = {x ** 2 for x in range(10)}
# set1
# {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
#
# type(set1)
# <class 'set'>

# Dictionary Comprehensions
# dict1 = {x : x ** 2 for x in range(10)}
# dict1
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
# type(dict1)
# <class 'dict'>