"""
Exercise 1:
Use while loop to print i as long as i is less than 6.
"""

# i = 1
# while i < 6:
#     print(i)
#     i += 1


"""
Exercise 2:
Stop the while loop if i is 3.
"""

# i = 1
# while i != 3:
#     print(i)
#     i += 1

"""
Exercise 3:
In the while loop, when i is 3, jump directly to the next iteration.
"""

# i = 0
# while i < 4:
#     i = i + 1
#     if i == 3:
#         continue
#     print(i)



"""
Exercise 4:
Loop through the items in the fruits list and print it.
"""
# fruits = ["apple", "banana", "cherry"]
# i = 0
# size = len(fruits)
# while i < size:
#     print(fruits[i])
#     i += 1
"""
Exercise 5:
In the loop, when the item value is "banana", jump directly to the next item.
"""

fruits = ["apple", "banana", "cherry"]

for x in fruits:
    if x == "banana":
        continue
    print(x)


"""
Exercise 6:
Use for loop and range function to print "Armenia" 6 times.
"""

# for i in range(6):
#     print("Armenia")

"""
Exercise 7:
Loop through the string and print all the characters except 2nd 'a' letter.
"""
# my_str = "Ararat"
# for char in my_str:
#     if char == "a":
#         continue
#     print(char)