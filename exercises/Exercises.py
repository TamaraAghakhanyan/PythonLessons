'''Basic Exercise for Beginners'''

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

import random, string

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
secret_letter = random.choice(letters)
p1, p2, p3, p4 = 26, 13, 7, 0

alphabet = dict()
for id, letter in enumerate(string.ascii_uppercase):
    alphabet[letter] = id + 1

rounds = 1
while rounds != 4:
    player_guess = input("Guess a letter from A - Z: ").upper()
    if rounds == 1 and player_guess == secret_letter:
        print(f"Congrats! You guessed the Secret Letter: '{secret_letter}' in Round {rounds}! You get {p1} points.")
        break
    elif rounds == 2 and player_guess == secret_letter:
        print(f"Congrats! You guessed the Secret Letter: '{secret_letter}' in Round {rounds}! You get {p2} points.")
        break
    elif rounds == 3 and player_guess == secret_letter:
        print(f"Congrats! You guessed the Secret Letter: '{secret_letter}' in Round {rounds}! You get {p3} points.")
        break
    elif rounds == 3 and player_guess != secret_letter:
        print(f"You failed to guess the secret letter, {secret_letter}, in time. You get {p4} points.")
        break
    else:
        if player_guess > secret_letter:
            print(f"Your guess, '{player_guess}' is too high.")
        elif player_guess < secret_letter:
            print(f"Your guess, '{player_guess}' is too low.")
    rounds += 1







