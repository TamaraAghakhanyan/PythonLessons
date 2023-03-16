#1. Print first 10 natural numbers using while loop
'''x = 1
while x <= 10:
    print(x)
    x = x + 1'''
import math
from math import factorial

#Exercise 1: Write a Python program to find those numbers which are divisible by 7 and
#multiple of 5,between 1500 and 2700 (both included)

'''for i in range(1500,2701):
    if i % 7 == 0 and i % 5 == 0:
        print(i, end=', ')'''


#8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
#Note : Use 'continue' statement.
#Expected Output : 0 1 2 4 5

'''for i in range(6):
     if i == 3:
        continue
     print(i, end=" ")'''

#10.Write a Python program which iterates the integers from 1 to 50.For multiples
#of three print "Fizz" instead of the number and for he multiples of five print "Buzz".
#For numbers which are multiples of both three and five print "FizzBuzz".

'''for i in range(51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)


x = 6
x += 3
print(x)
import random
print(dir(random))'''




















# Exercise 1: Print First 10 natural numbers using while loop
# Expected output:
#
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1

# Exercise 2: Print the following pattern
# Write a program to print the following number pattern using a loop.
#
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# rows = 5
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j,  end=" ")
#     print("")


'''Exercise 3: Calculate the sum of all numbers from 1 to a given number
Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)

Expected Output:

Enter number 10
Sum is:  55'''

# n = int(input("Enter a number: "))
# sum = 0
#
# for i in range(1, n + 1):
#     sum = sum + i
# print(sum)

# num = int(input("Enter a number: "))
# a = sum(range(1, num + 1))
# print(a)

'''Exercise 4: Write a program to print multiplication table of a given number
For example, num = 2 so the output should be

2
4
6
8
10
12
14
16
18
20'''

# for i in range(1, 11):
#     a = i * 2
#     print(a)

'''Exercise 5: Display numbers from a list using loop
Write a program to display only those numbers from a list that satisfy the following conditions


The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop
Given:

numbers = [12, 75, 150, 180, 145, 525, 50]
Expected output:

75
150
145'''

# numbers = [12, 75, 150, 180, 145, 525, 50]
#
# for i in numbers:
#     if i > 500:
#         break
#     elif i > 150:
#         continue
#     elif i % 5 == 0:
#         print(i)

'''Exercise 6: Count the total number of digits in a number
Write a program to count the total number of digits in a number using a while loop.

For example, the number is 75869, so the output should be 5.'''

# number = 75869
# counter = 0
#
# while number != 0:
#     number = number // 10
#     counter = counter + 1
# print(counter)


'''Exercise 7: Print the following pattern
Write a program to use for loop to print the following reverse number pattern

5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1'''

# rows = 5
# for i in reversed(range(1, rows + 1)):
#     for j in reversed(range(1, i + 1)):
#         print(j,  end=" ")
#     print("")


'''Exercise 8: Print list in reverse order using a loop
Given:

list1 = [10, 20, 30, 40, 50]
Expected output:


50
40
30
20
10'''

# list1 = [10, 20, 30, 40, 50]
# for i in reversed(list1):
#     print(i)

'''Exercise 9: Display numbers from -10 to -1 using for loop
Expected output:

-10
-9
-8
-7
-6
-5
-4
-3
-2
-1'''

# for i in range(-10, 0, 1):
#     print(i)

'''Exercise 10: Use else block to display a message “Done” after successful execution of for loop
For example, the following loop will execute without any error.

Given:

for i in range(5):
    print(i)
Expected output:

0
1
2
3
4
Done!'''

# for i in range(5):
#     print(i)
# else:
#     print("Done!")


'''Exercise 11: Write a program to display all prime numbers within a range

Note: A Prime Number is a number that cannot be made by multiplying other whole numbers. A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers

Examples:

6 is not a prime mumber because it can be made by 2×3 = 6
37 is a prime number because no other whole numbers multiply together to make it.
Given:
# range
start = 25
end = 50
Expected output:

Prime numbers between 25 and 50 are:
29
31
37
41
43
47'''

# start = 25
# end = 50
#
# for num in range(start, end + 1):
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)


'''Exercise 12: Display Fibonacci series up to 10 terms
The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.

For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34.

Expected output:

Fibonacci sequence:
0  1  1  2  3  5  8  13  21  34'''

# num1 = 0
# num2 = 1
# res = 0
# for i in range(10):
#     print(num1, end="  ")
#     res = num1 + num2
#
#     num1 = num2
#     num2 = res



'''Exercise 13: Find the factorial of a given number
Write a program to use the loop to find the factorial of a given number.

The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.

For example: calculate the factorial of 5

5! = 5 × 4 × 3 × 2 × 1 = 120
120'''

# number = 5
# fact = 1
#
# if number <= 0:
#     print("invalid number")
# else:
#     for x in range(1, number + 1):
#         fact = fact * x
#     print(fact)

'''Exercise 14: Reverse a given integer number
Given:

76542

Expected output:

24567'''

# a = 76542
#
#
# for i in str(a)[::-1]:
#     print(i, end="")

'''Exercise 15: Use a loop to display elements from a given list present at odd index positions
Given:

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

Expected output:
20 40 60 80 100'''

# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# # for i in my_list:
# #     if my_list.index(i) % 2 == 0:
# #         continue
# #     else:
# #         print(i)
#
# for i in my_list[1::2]:
#     print(i, end=" ")


'''Exercise 16: Calculate the cube of all numbers from 1 to a given number
Write a program to print the cube of all numbers from 1 to a given number

Given:

input_number = 6

Expected output:

Current Number is : 1  and the cube is 1
Current Number is : 2  and the cube is 8
Current Number is : 3  and the cube is 27
Current Number is : 4  and the cube is 64
Current Number is : 5  and the cube is 125
Current Number is : 6  and the cube is 216'''

# a = int(input("Enter a number: "))
#
# for i in range(1, a + 1):
#     cube = i * i * i
#     print("Current Number is :", i, "and the cube is ", cube)

'''Exercise 17: Find the sum of the series upto n terms
Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 
2 + 22 + 222 + 2222 + 22222 = 24690

Given:

# number of terms
n = 5
Expected output:
24690'''

number_of_terms = 5
print(sum(int('2' * (i + 1)) for i in range(number_of_terms)))



