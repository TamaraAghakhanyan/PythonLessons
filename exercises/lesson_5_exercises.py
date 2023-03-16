"""
Exercise 1:
Turn every item of a list into its square.
Given a list of numbers. write a program to turn 
every item of a list into its square.

"""
numbers = [1, 2, 3, 4, 5, 6, 7]
# output [1, 4, 9, 16, 25, 36, 49]
x = []
for i in numbers:
   a = i**2
   x.append(a)

print(x)


# code goes here

"""
Exercise 2:
Write a program to create a new string 
made of an input string’s first, middle, and last character. Use input().
"""
# Ex. str1 = "James" output 'Jms'

# a = input("enter something: ")
#
# for i in a:
#    if len(a) % 2 == 0:
#       x1 = a[0]
#       x2 = a[(len(a) - 1) // 2]
#       x3 = a[len(a) // 2]
#       x4 = a[-1]
#       x = x1 + x2 + x3 + x4
#    else:
#       x1 = a[0]
#       x2 = a[len(a) // 2]
#       x3 = a[-1]
#       x = x1 + x2 + x3
# print(x)












"""
Exercise 3:
Given two integer numbers return their power(քառակուսի) 
only if the product is equal to or lower than 1000, else return their sum.
"""
number1 = 20
number2 = 30
# result 600
number1 = 40
number2 = 30
# result 70

# code goes here

"""
Exercise 4: 
Write a function to return True if the first
and last number of a given list is same. 
If numbers are different then return False.
"""
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

print(numbers_y[0] == numbers_y[-1] or "False")
print(numbers_x[0] == numbers_x[-1] or "False")


"""
Exercise 5: 
A company decided to give bonus of '5%' to employee 
if his/her year of service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount. 
"""
# a = int(input("Enter your salary: "))
# b = int(input("Enter your year of service: "))
#
# if b > 5:
#    bonus = a/5 * 100
#    print(bonus)
# else:
#    print("Sorry, you won't get bonus:/")



"""
Exercise 6:
Take values of length and breadth of a rectangle 
from user and check if it is square or not.
"""
a = int(input("Enter length: "))
b = int(input("Enter breadth: "))

if a == b:
   print("It is square")
else:
   print("It is not square")
