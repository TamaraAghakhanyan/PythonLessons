''''Basic Exercise for Beginners'''
from curses.ascii import isalpha

'''Exercise 1: Calculate the multiplication and sum of two numbers
Given two integer numbers, return their product only if the product
is equal to or lower than 1000. Otherwise, return their sum.

Given 1:

number1 = 20
number2 = 30

Expected Output:

The result is 600
Given 2:

number1 = 40
number2 = 30
Expected Output:

The result is 70'''


# if number1 * number2 <= 1000:
#     print(number1 * number2)
# else:
#     print(number1 + number2)


'''Exercise 2: Print the sum of the current number and the previous number
Write a program to iterate the first 10 numbers, and in each iteration, 
print the sum of the current and previous number.

Expected Output:

Printing current and previous number sum in a range(10)
Current Number 0 Previous Number  0  Sum:  0
Current Number 1 Previous Number  0  Sum:  1
Current Number 2 Previous Number  1  Sum:  3
Current Number 3 Previous Number  2  Sum:  5
Current Number 4 Previous Number  3  Sum:  7
Current Number 5 Previous Number  4  Sum:  9
Current Number 6 Previous Number  5  Sum:  11
Current Number 7 Previous Number  6  Sum:  13
Current Number 8 Previous Number  7  Sum:  15
Current Number 9 Previous Number  8  Sum:  17'''

# print("Printing current and previous number sum in a range(10)")
# for i in range(0, 10):
#     if i == 0:
#         print("Current Number", i, "Previous Number", i, "Sum:  ", i + i)
#     else:
#         print("Current Number", i , "Previous Number", i - 1, "Sum:  ", i + i - 1)


'''Exercise 3: Print characters from a string that are present at an even index number
Write a program to accept a string from the user and display characters that are present
at an even index number.

For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

Expected Output:

Orginal String is  pynative
Printing only even index chars
p
n
t
v'''

# string1 = input("Original String is  ")
#
# x = len(string1)
# print("Printing only even index chars")
#
# for i in range(0, x - 1, 2):
#     print(string1[i])


'''Exercise 4: Remove first n characters from a string
Write a program to remove characters from a string starting 
from zero up to n and return a new string.

For example:

remove_chars("pynative", 4) so output must be tive. 
Here, we need to remove the first four characters from a string.
remove_chars("pynative", 2) so output must be native. 
Here, we need to remove the first two characters from a string.
Note: n must be less than the length of the string.

'''

# string1 = input("input a string: ")
# n = int(input("Character count to be removed: "))
#
# if n < len(string1):
#     string2 = str(string1[n:])
#     print(string2)
#     print(type(string2))
# else:
#     print("Oops! Wrong Character count is inserted")


'''Exercise 5: Check if the first and last number of a list is the same
Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

Given:

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
Expected Output:

Given list: [10, 20, 30, 40, 10]
result is True

numbers_y = [75, 65, 35, 75, 30]
result is False'''

# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]
#
#
# if numbers_x[0] == numbers_x[len(numbers_x) - 1]:
#     print("Given list: ", numbers_x)
#     print("result is True")
# else:
#     print("Given list: ", numbers_x)
#     print("result is False")
#
#
# if numbers_y[0] == numbers_x[len(numbers_y) - 1]:
#     print("Given list: ", numbers_y)
#     print("result is True")
# else:
#     print("Given list: ", numbers_y)
#     print("result is False")


'''Exercise 6: Display numbers divisible by 5 from a list
Iterate the given list of numbers and print only those numbers which are divisible by 5

Expected Output:

Given list is  [10, 20, 33, 46, 55]
Divisible by 5
10
20
55'''

# print("Given list is  ", [10, 20, 33, 46, 55])
# print("Divisible by 5")
#
# for i in [10, 20, 33, 46, 55]:
#     if i % 5 == 0:
#         print(i)


'''Exercise 7: Return the count of a given substring from a string
Write a program to find how many times substring “Emma” appears in the given string.

Given:

str_x = "Emma is good developer. Emma is a writer"
Expected Output:

Emma appeared 2 times'''

# str_x = "Emma is good developer. Emma is a writer"
#
# a = str_x.count("Emma")
# print("Emma appeared", a, "times")


'''Exercise 8: Print the following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5'''

# n = 5
# for x in range(n + 1):
#     for y in range(x):
#         print(x, end=" ")
#     print("")


'''Exercise 9: Check Palindrome Number
Write a program to check if the given number is a palindrome number.

A palindrome number is a number that is the same after reverse. 
For example, 545, is the palindrome numbers

Expected Output:

original number 121
Yes. given number is palindrome number

original number 125
No. given number is not palindrome number'''


# number1 = input("original number ")
# number2 = str(number1)[::-1]
#
#
# if number1 != number2:
#     print("No. given number is not palindrome number")
# else:
#     print("Yes. given number is palindrome number")


'''Exercise 10: Create a new list from two list using the following condition
Create a new list from two list using the following condition

Given two list of numbers, write a program to create a new list such that the new list should contain 
odd numbers from the first list and even numbers from the second list.

Given:

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
Expected Output:

result list: [25, 35, 40, 60, 90]'''

# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
#
# result = []
#
# for i in list1:
#     if i % 2 != 0:
#         result.append(i)
#
# for j in list2:
#     if j % 2 == 0:
#         result.append(j)
#
# print(result)


'''Exercise 11: Write a Program to extract each digit from 
an integer in the reverse order.
For example, If the given int is 7536, the output shall 
be “6 3 5 7“, with a space separating the digits.'''


# x = input("Given number: ")
# y = str(x)[::-1]
#
# result = y.replace("", " ").strip()
#
# print("Result: ", result)


'''Exercise 12: Calculate income tax for the given income by adhering to the rules below
Taxable Income	Rate (in %)
First $10,000	0
Next $10,000	10
The remaining	20
Expected Output:

For example, suppose the taxable income is 45000, and the income tax payable is

10000*0% + 10000*10%  + 25000*20% = $6000.'''


# a = int(input("Income: "))
#
#
# x = int(10000 * 0/100 + 10000 * 10/100 + (a - 20000) * 20/100)
# print("Income tax: ", x)


'''Exercise 13: Print multiplication table from 1 to 10
Expected Output:
1  2 3 4 5 6 7 8 9 10 		
2  4 6 8 10 12 14 16 18 20 		
3  6 9 12 15 18 21 24 27 30 		
4  8 12 16 20 24 28 32 36 40 		
5  10 15 20 25 30 35 40 45 50 		
6  12 18 24 30 36 42 48 54 60 		
7  14 21 28 35 42 49 56 63 70 		
8  16 24 32 40 48 56 64 72 80 		
9  18 27 36 45 54 63 72 81 90 		
10 20 30 40 50 60 70 80 90 100 '''


# for i in range(1,11):
#     for j in range(1,11):
#         print(i * j, end=" ")
#     print("")

'''Exercise 14: Print a downward Half-Pyramid Pattern of Star (asterisk)
* * * * *  
* * * *  
* * *  
* *  
*
'''

# row = 5
# for i in range(0, row + 1):
#     for j in range(row - i, 0, -1):
#         print("*", end=" ")
#     print("")


'''Exercise 15: Write a function called exponent(base, exp) that returns
an int value of base raises to the power of exp.
Note here exp is a non-negative integer, and the base is an integer.

Expected output

Case 1:

base = 2
exponent = 5

2 raises to the power of 5: 32 i.e. (2 *2 * 2 *2 *2 = 32)


Case 2:

base = 5
exponent = 4

5 raises to the power of 4 is: 625
i.e. (5 *5 * 5 *5 = 625)'''

# base = int(input("base = "))
# exp = int(input("exponent = "))
# def exponent(base, exp):
#     res = base ** exp
#     print( base, "raises to the power of ", exp, "is:", res)
#
#
# exponent(base, exp)

'''Python Input and Output Exercise'''

'''Exercise 1: Accept numbers from a user
Write a program to accept two numbers from the user and calculate multiplication'''

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))
# result = num1 * num2
# print("The result is: ", result)

'''Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”
Use the print() function to format the given words in the mentioned format. 
Display the ** separator between each string.

Expected Output:

For example: print('Name', 'Is', 'James') will display Name**Is**James'''


# str1 = ("Name", "Is", "James")
# result = "**".join(str1)
# print(result)

'''Exercise 3: Convert Decimal number to octal using print() output formatting
Given:

num = 8
Expected Output:

The octal number of decimal number 8 is 10'''

# num = 8
# print("The octal number of decimal number", num, "is ", oct(num))


'''Exercise 4: Display float number with 2 decimal places using print()
Given:

num = 458.541315
Expected Output:

458.54'''

# num = 458.541315
# print("{:.2f}".format(num))

'''Exercise 5: Accept a list of 5 float numbers as an input from the user

Expected Output:

[78.6, 78.6, 85.3, 1.2, 3.5]'''

# num1 = float(input("Number 1: "))
# num2 = float(input("Number 2: "))
# num3 = float(input("Number 3: "))
# num4 = float(input("Number 4: "))
# num5 = float(input("Number 5: "))
#
# list1= []
# list1.append(num1)
# list1.append(num2)
# list1.append(num3)
# list1.append(num4)
# list1.append(num5)
# print(list1)

# OR:

# numbers = []

# for i in range(0, 5):
#     print("Enter number at location", i, ":")
#     item = float(input())
#     numbers.append(item)
#
# print("User List:", numbers)

'''Exercise 6: Write all content of a given file into a new file by 
skipping line number 5

Create a test.txt file and add the below content to it.

Given test.txt file:

line1
line2
line3
line4
line5
line6
line7

Expected Output: new_file.txt

line1
line2
line3
line4
line6
line7'''


# with open("test.txt", "w") as file:
#     file.write("line1\n")
#     file.write("line2\n")
#     file.write("line3\n")
#     file.write("line4\n")
#     file.write("line5\n")
#     file.write("line6\n")
#     file.write("line7\n")
#     file.write("line8\n")
# print(file)
#
# with open("test.txt", "r") as file:
#     content = file.read()
#
# with open("new_file.txt", "w") as new:
#     count = 0
#     for line in content.splitlines():
#         if count == 4:
#             count += 1
#             continue
#         else:
#             new.write(line + "\n")
#         count += 1


'''Exercise 7: Accept any three string from one input() call
Write a program to take three names as input from a user in
the single input() function call.

Expected Output

Enter three string Emma Jessa Kelly
Name1: Emma
Name2: Jessa
Name3: Kelly'''

# name1, name2, name3 = input("Enter Name1, Name2, Name3").split()
# print("Name1: ", name1, "\nName2: ", name2, "\nName3: ", name3)


'''Exercise 8: Format variables using a string.format() method.
Write a program to use string.format() method to format the following three variables as per the expected output

Given:

totalMoney = 1000
quantity = 3
price = 450

Expected Output:

I have 1000 dollars so I can buy 3 football for 450.00 dollars.'''

# totalMoney = 1000
# quantity = 3
# price = 450
#
# result = "I have {} dollars so I can buy {} football for {} dollars".format(totalMoney, quantity, price)
# print(result)

'''Exercise 9: Check file is empty or not
Write a program to check if the given file is empty or not'''

# with open("new_file.txt", "r") as new:
#     new.read()
#
# import os
#
# file_path = '/Users/tamaraaghakhanyan/MyPythonLessons/lessons/python/exercises/new_file.txt'
#
# if os.path.getsize("/Users/tamaraaghakhanyan/MyPythonLessons/lessons/python/exercises/new_file.txt") == 0:
#     print("The file is empty.")
# else:
#     print("The file is not empty.")

'''Exercise 10: Read line number 4 from the following file

Create a test.txt file and add the below content to it.

test.txt file:

line1
line2
line3
line4
line5
line6
line7'''

# file_path = "/Users/tamaraaghakhanyan/MyPythonLessons/lessons/python/exercises/test.txt"
#
# import linecache
# res = linecache.getline(file_path, 4)
# print(res)

'''A person is playing a guessing game in which they have 3 guesses to 
figure out the computer’s secret letter which will be between A and Z inclusive. 
If they guess the letter correctly on the first guess the program should stop making 
them guess and they should get 26 points. If they guess the letter correctly on the 
second guess the program should stop making them guess and they should get 13 points. 
If they guess the letter correctly on the third guess, they should get 7 points. 
After an incorrect guess tell the user if their guess was too high or too low based on 
the results of checkGuess. If they fail to guess the letter correctly after 
3 guesses they get 0 points. Be sure to tell them what score they got.'''

# import random, string
#
# letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
# 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# secret_letter = random.choice(letters)
# p1, p2, p3, p4 = 26, 13, 7, 0
#
# alphabet = dict()
# for id, letter in enumerate(string.ascii_uppercase):
#     alphabet[letter] = id + 1
#
# rounds = 1
# while rounds != 4:
#     player_guess = input("Guess a letter from A - Z: ").upper()
#     if rounds == 1 and player_guess == secret_letter:
#         print(f"Congrats! You guessed the Secret Letter: '{secret_letter}' in Round {rounds}! You get {p1} points.")
#         break
#     elif rounds == 2 and player_guess == secret_letter:
#         print(f"Congrats! You guessed the Secret Letter: '{secret_letter}' in Round {rounds}! You get {p2} points.")
#         break
#     elif rounds == 3 and player_guess == secret_letter:
#         print(f"Congrats! You guessed the Secret Letter: '{secret_letter}' in Round {rounds}! You get {p3} points.")
#         break
#     elif rounds == 3 and player_guess != secret_letter:
#         print(f"You failed to guess the secret letter, {secret_letter}, in time. You get {p4} points.")
#         break
#     else:
#         if player_guess > secret_letter:
#             print(f"Your guess, '{player_guess}' is too high.")
#         elif player_guess < secret_letter:
#             print(f"Your guess, '{player_guess}' is too low.")
#     rounds += 1


'''Python Loop Exercises'''

'''Exercise 1: Print First 10 natural numbers using while loop

xpected output:

1
2
3
4
5
6
7
8
9
10'''


# a = 1
# while a < 11:
#     print(a)
#     a += 1

'''Exercise 2: Print the following pattern
Write a program to print the following number pattern using a loop.

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5'''

# row = 5
# for i in range(1,row + 1, 1):
#     for j in range(1, i + 1):
#         print(j, end= " ")
#     print("")

'''Practice: Print a rectangle Pattern with 5 rows and 3 columns of stars
Solve the below Python nested loop exercise.

Print following rectangle of stars

***
***
***
***
***'''

# row = 5
# for i in range(1, row + 1):
#     count = 0
#     while count < 3:
#         print("*", end= "")
#         count += 1
#     print()


'''if you had two lists and want to get all combinations of them, 
To achieve this, you need to use two nested loops as mentioned below.'''

# first = [2, 3, 4]
# second = [20, 30, 40]
# final = []
# for i in first:
#     for j in second:
#         final.append(i+j)
# print(final)
#
# # OR
#
# final = [i + j for i in first for j in second]
# print(final)

# final = [[x, y] for x in [10, 20, 30] for y in [30, 10, 50] if x != y]
# print(final)

'''Exercise 3: Calculate the sum of all numbers from 1 to a given number
Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)

Expected Output:

Enter number 10
Sum is:  55
'''

# num = int(input("Enter a number: "))
#
# sum = 0
#
# for i in range(1, num + 1):
#     sum = sum + i
# print("Sum is: ", sum)

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

# num = 2
# result = 0
# for i in range(1, 11):
#     result = i * num
#     print(result)

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


# number = input("Enter a number: ")
#
# a = len(number)
# print(a)

# OR


# num = 75869
# count = 0
# while num != 0:
#     # floor division
#     # to reduce the last digit from number
#     num = num // 10
#
#     # increment counter by 1
#     count = count + 1
# print("Total digits are:", count)

'''Exercise 7: Print the following pattern
Write a program to use for loop to print the following reverse number pattern

5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1'''

# row = 5
#
# for i in range(row, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end= " ")
#     print()

'''Exercise 8: Print list in reverse order using a loop
Given:
list1 = [10, 20, 30, 40, 50]
Expected output:

50
40
30
20
10

'''


# list1 = [10, 20, 30, 40, 50]
#
# for i in reversed(list1):
#     print(i)

# or

# size = len(list1) - 1
# for i in range(size, -1, -1):
#     print(list1[i])

''''Exercise 9: Display numbers from -10 to -1 using for loop
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

'''Exercise 10: Use else block to display a message “Done” after successful 
execution of for loop
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
#
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

# start = int(input("Start: "))
# end = int(input("End: "))
#
# print("Prime numbers between", start, "and ", end, "are:")
#
# for num in range(start, end +1, 1):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num)

''''Exercise 12: Display Fibonacci series up to 10 terms
The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.

For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34.

Expected output:

Fibonacci sequence:
0  1  1  2  3  5  8  13  21  34'''

# num1 = 0
# num2 = 1
#
# print("Fibonacci sequence: ")
# for i in range(10):
#     print(num1, end= " ")
#     result = num1 + num2
#     num1 = num2
#     num2 = result


'''Exercise 13: Find the factorial of a given number
Write a program to use the loop to find the factorial of a given number.

The factorial (symbol: !) means to multiply all whole numbers from the chosen 
number down to 1.
'''

# n = int(input("Enter the number to calculate the factorial: "))
#
# factorial = 1
#
# for i in range(1, n + 1):
#     factorial = factorial * i
# print(factorial)


'''Exercise 14: Reverse a given integer number
Given:

76542

Expected output:

24567'''

# n = str(input("Enter the number: "))
# result = int(str(n)[::-1])
# print(result)
#
#
# OR
#
# num = 76542
# reverse_number = 0
# print("Given Number ", num)
# while num > 0:
#     reminder = num % 10
#     reverse_number = (reverse_number * 10) + reminder
#     num = num // 10
# print("Revere Number ", reverse_number)


'''Exercise 15: Use a loop to display elements from a given 
list present at odd index positions

Given:

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


Expected output:

20 40 60 80 100

'''
#
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#
# for i in range(len(my_list)):
#     if i != 0 and i % 2 != 0:
#         print(my_list[i], end= " ")

'''Exercise 16: Calculate the cube of all numbers from 1 to a given number
Write a program to rint the cube of all numbers from 1 to a given number

Given:

input_number = 6

Expected output:

Current Number is : 1  and the cube is 1
Current Number is : 2  and the cube is 8
Current Number is : 3  and the cube is 27
Current Number is : 4  and the cube is 64
Current Number is : 5  and the cube is 125
Current Number is : 6  and the cube is 216'''

# current_number = int(input("Enter a number: "))
#
# for i in range(1, current_number + 1):
#     cube = i ** 3
#     print("Current Number is :", i, "and the cube is ", cube)


'''Exercise 17: Find the sum of the series upto n terms
Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

Given:

# number of terms
n = 5
Expected output:


24690'''


# n = 5
# res = 2
# sum = 0
# sum1 = 0
#
#
# result = 2
# for i in range(0, n):
#     count = res * (10 ** i)
#     sum = sum + count
#     sum1 = sum1 + sum
# print(sum1)


'''Exercise 18: Print the following pattern
Write a program to print the following start pattern using the for loop

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
'''
# row = 5
#
# for i in range(1,row + 1, 1):
#     for j in range(1, i + 1):
#         print("*", end= " ")
#     print("")
# for i in range(row -1, 0, -1):
#     for j in range(i, 0, -1):
#         print("*", end=" ")
#     print("")


'''Python Functions Exercises'''

'''Exercise 1: Create a function in Python
Write a program to create a function that takes two arguments, name and age, 
and print their value.'''


# def func1(name, age):
#     return (name, age)
#
# print(func1("Toma", 29))


''' 
Exercise 2: Create a function with variable length of arguments
Write a program to create function func1() to accept a variable length of arguments and print their value.

Note: Create a function in such a way that we can pass any number of arguments to this function, and the function should process them and display each argument’s value.

Read: variable length of arguments in functions

Function call:


# call function with 3 arguments
func1(20, 40, 60)

# call function with 2 arguments
func1(80, 100)
Expected Output:

Printing values
20
40
60


Printing values
80
100

'''

# def function(*args):
#     return args
#
# print(function(20, 40, 60))
# print(function(80, 100))



'''Exercise 3: Return multiple values from a function
Write a program to create function calculation() such that it can accept
two variables and calculate addition and subtraction. Also, it must return 
both addition and subtraction in a single return call.

Given:

def calculation(a, b):
    # Your Code

res = calculation(40, 10)
print(res)
Expected Output

50, 30'''

# def calculation(a, b):
#     return (a + b, a - b)
#
# print(calculation(40, 10))


'''Exercise 4: Create a function with a default argument
Write a program to create a function show_employee() using the following conditions.

It should accept the employee’s name and salary and display both.
If the salary is missing in the function call then assign default value 9000 to salary
See: Default arguments in function

Given:

showEmployee("Ben", 12000)
showEmployee("Jessa")
Expected output:

Name: Ben salary: 12000
Name: Jessa salary: 9000'''


# def show_employee(name, salary = 9000):
#     print("Name: ", name, "salary: ", salary)
#
# show_employee("Ben", 12000)
# show_employee("Jessa")


'''Exercise 5: Create an inner function to calculate the addition in 
the following way

    Create an outer function that will accept two parameters, a and b
    Create an inner function inside an outer function that will calculate 
the addition of a and b
    At last, an outer function will add 5 into addition and return it'''

# def func1(a, b):
#     def addition(a, b):
#         return a + b
#     return 5 + addition(a, b)
#
# print(func1(10, 5))


'''Exercise 6: Create a recursive function
Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

A recursive function is a function that calls itself again and again.

Expected Output:

55'''

# def sum(a):
#     if a:
#         return a + sum(a - 1)
#     else:
#         return 0
#
# res = sum(10)
# print(res)

'''Exercise 7: Assign a different name to function and call it through the new name
Below is the function display_student(name, age). Assign a new name show_tudent(name, age) to it and call it using the new name.

Given:


def display_student(name, age):
    print(name, age)

display_student("Emma", 26)
You should be able to call the same function using

show_student(name, age)
'''

# '''option 1'''
# def display_student(name, age):
#     print(name, age)
#
#
# def show_student(name, age):
#     return display_student(name, age)
#
# show_student("Emma", 26)
#
#
# '''option 2'''
#
# def display_student(name, age):
#     print(name, age)
#
# show_student = display_student
# show_student("Emma", 26)


'''Exercise 8: Generate a Python list of all the even numbers between 4 to 30
Expected Output:

[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]'''


# def even_numbers(a, b):
#     even_list = []
#     for i in range(a, b):
#         if i % 2 == 0:
#             even_list.append(i)
#     return even_list
#
#
# result = even_numbers(4, 30)
# print(result)
#
# # OR
#
# print(list(range(4, 30, 2)))


'''Exercise 9: Find the largest item from a given list
x = [4, 6, 8, 24, 12, 2]
Expected Output:

24'''

# x = [4, 6, 8, 24, 12, 2]
#
# print(max(x))


'''Python String Exercises'''


'''Exercise 1A: Create a string made of the first, middle and last character
Write a program to create a new string made of an input string’s first, middle, and last character.

Given:

str1 = "James"
Expected Output:

Jms'''
#
# str1 = "James"
#
# num = int(len(str1) / 2)
# str2 = str1[0]
# str2 = str2 + str1[num] + str1[-1]
#
# print(str2)


'''Exercise 1B: Create a string made of the middle three characters
Write a program to create a new string made of the middle three characters of an input string.

Given:

Case 1

str1 = "JhonDipPeta"
Output

Dip
Case 2

str2 = "JaSonAy"
Output

Son'''

# str1 = input("Enter a string No 1: ")
# str2 = input("Enter a string No 2: ")
#
# l1 = len(str1)
# l2 = len(str2)
#
# mid_char1 = int(l1 / 2)
# mid_char2 = int(l2 / 2)
#
# res1 = str1[mid_char1 - 1 : mid_char1 + 2]
# res2 = str2[mid_char2 - 1 : mid_char2 + 2]
#
# print("middle three characters of string No 1: ", res1)
# print("middle three characters of string No 2: ", res2)

'''Exercise 2: Append new string in the middle of a given string
Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

Given:

s1 = "Ault"
s2 = "Kelly"
Expected Output:

AuKellylt'''

# s1 = "Ault"
# s2 = "Kelly"
#
# mid_s1 = int(len(s1) / 2)
# part1 = s1[: mid_s1]
# part2 = s1[mid_s1 :]
# s3 = part1 + s2 + part2
# print(s3)


'''Exercise 3: Create a new string made of the first, middle, and last characters of each input string

Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.

Given:

s1 = "America"
s2 = "Japan"
Expected Output:

AJrpan'''

# s1 = "America"
# s2 = "Japan"
#
# mid_s1 = int(len(s1) / 2)
# mid_s2 = int(len(s2) / 2)
#
# new_str = s1[0] + s2[0] + s1[mid_s1] + s2[mid_s2] + s1[-1] + s2[-1]
# print(new_str)


'''Exercise 4: Arrange string characters such that lowercase letters should come
first
Given string contains a combination of the lower and upper case letters. 
Write a program to arrange the characters of a string so that all lowercase letters 
should come first.

Given:

str1 = "PyNaTive"

Expected Output:

yaivePNT'''


# str1 = "PyNaTive
# s1 = str()
# s2 = str()
# for i in str1:
#     if i.islower():
#         s1 = s1 + i
#     else:
#         s2 = s2 + i
#
# result = s1 + s2
# print(result)

'''Exercise 5: Count all letters, digits, and special symbols from a given string
Given:

str1 = "P@#yn26at^&i5ve"
Expected Outcome:

Total counts of chars, digits, and symbols 

Chars = 8 
Digits = 3 
Symbol = 4'''


# str1 = "P@#yn26at^&i5ve"
#
# chars = 0
# digits = 0
# symbols = 0
#
# print("Total counts of chars, digits, and symbols")
#
# for i in str1:
#     if isalpha(i):
#         chars = chars + 1
#     elif i.isdigit():
#         digits = digits + 1
#     else:
#         symbols = symbols + 1
#
# print("Chars =", chars, "\n""Digits =", digits, "\n""Symbol =", symbols)


'''Exercise 6: Create a mixed String using the following rules
Given two strings, s1 and s2. Write a program to create a new string s3 
made of the first char of s1, then the last char of s2, Next, 
the second char of s1 and second last char of s2, and so on. 
Any leftover chars go at the end of the result.

Given:

s1 = "Abc"
s2 = "Xyz"
Expected Output:

AzbycX'''

'''s1 = "Abc"
s2 = "Xyz"

# get string length
s1_length = len(s1)
s2_length = len(s2)

# get length of a bigger string
length = s1_length if s1_length > s2_length else s2_length
result = ""

# reverse s2
s2 = s2[::-1]

# iterate string
# s1 ascending and s2 descending
for i in range(length):
    if i < s1_length:
        result = result + s1[i]
    if i < s2_length:
        result = result + s2[i]

print(result)'''


''''Exercise 7: String characters balance Test
Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. The character’s position doesn’t matter.

Given:


Case 1:

s1 = "Yn"
s2 = "PYnative"
Expected Output:

True
Case 2:

s1 = "Ynf"
s2 = "PYnative"
Expected Output:

False'''

'''Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
Write a program to find all occurrences of “USA” in a given string ignoring the case.

Given:

str1 = "Welcome to USA. usa awesome, isn't it?"
Expected Outcome:


The USA count is: 2'''

# str1 = "Welcome to USA. usa awesome, isn't it?"
# s1 = str1.lower()
# count = s1.count("usa")
#
# print("The USA count is: ", count)


'''Exercise 9: Calculate the sum and average of the digits present in a string
Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.

Given:

str1 = "PYnative29@#8496"
Expected Outcome:

Sum is: 38 Average is  6.333333333333333'''

# str1 = "PYnative29@#8496"
#
# count = 0
# x = 0
# list1 = []
# for i in str1:
#     if i.isdigit():
#         count = count + 1
#         x = int(i)
#         list1.append(x)
#
# s = sum(list1)
# a = s / count
#
# print("Sum:", s, "Average:", a)


'''Exercise 10: Write a program to count occurrences of all characters within a string
Given:

str1 = "Apple"
Expected Outcome:

{'A': 1, 'p': 2, 'l': 1, 'e': 1}'''

# str1 = "Apple"
# dict1 = {}
# key = str()
# value = int()
#
# for i in str1:
#     key = i
#     value = str1.count(i)
#     dict1.update({key:value})
#
# print(dict1)


'''Exercise 11: Reverse a given string
Given:

str1 = "PYnative"
Expected Output:

evitanYP'''

# str1 = "PYnative"
# print(str1[:: -1])

'''Exercise 12: Find the last position of a given substring
Write a program to find the last position of a substring “Emma” in a given string.

Given:

str1 = "Emma is a data scientist who knows Python. Emma works at google."
Expected Output:

Last occurrence of Emma starts at index 43'''

# str1 = "Emma is a data scientist who knows Python. Emma works at google."
# x = str1.rfind("Emma")
# print("Last occurrence of Emma starts at index", x)


'''Exercise 13: Split a string on hyphens
Write a program to split a given string on hyphens and display each substring.

Given:

str1 = Emma-is-a-data-scientist
Expected Output:

Displaying each substring

Emma
is
a
data
scientist'''


# str1 = "Emma-is-a-data-scientist"
# #
# # res = str1.split("-",)
# #
# # print("Displaying each substring", "\n")
# #
# # for i in res:
# #     print(i)

'''Exercise 14: Remove empty strings from a list of strings
Given:

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
Expected Output:

Original list of sting
['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']

After removing empty strings
['Emma', 'Jon', 'Kelly', 'Eric']'''


# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
#
# new_list = []
#
# for i in str_list:
#     if i:
#         new_list.append(i)
#
# print(new_list)

'''Exercise 15: Remove special symbols / punctuation from a string
Given:

str1 = "/*Jon is @developer & musician"
Expected Output:'''


str1 = "/*Jon is @developer & musician"

for i in str1:
    if isalpha(i):
        pass
    elif i == " ":
        pass
    else:
        filter(i)
















