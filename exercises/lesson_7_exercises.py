"""
Exercise 1:
Write a program to count the total number of digits in a number using a while loop.
For example, the number is 75869, so the output should be 5.

"""

# code goes here

"""
Exercise 2:
Write a program to use for loop to print the following reverse number pattern
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
"""

# code goes here

"""
Exercise 3:
Print list in reverse order using a loop
50
40
30
20
10
"""
#

"""
Exercise 4:
Concatenate two lists index-wise.
Write a program to add two lists index-wise. 
Create a new list that contains the 0th index item from both the list, 
then the 1st index item, and so on till the last element.
Any leftover items will get added at the end of the new list.
Expected output ['My', 'name', 'is', 'Kelly']
"""
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
#
# list3 = [i + j for i, j in zip(list1, list2)]
# print(list3)







"""
Exercise 5:
Write a programm that loops given.
If the number is divisible by 3, it should return “Fizz”.
If it is divisible by 5, it should return “Buzz”.
If it is divisible by both 3 and 5, it should return “FizzBuzz”.
Otherwise, it should return the same number.
"""

# list1 = [10, 20, 30, 40, 50]
#
# for i in list1:
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")



"""
Exercise 6:
Write a Python program to find the first appearance of the substring "not" and "poor" from a given string. 
If "not" follows the "poor", replace the whole "not"..."poor" substring with "good". Return the resulting string.
Ex.1
   Sample String : "The lyrics is not that poor!"
   Expected Result : "The lyrics is good!" 
Ex.2
   Sample String : "The lyrics is poor!"
   Expected Result : "The lyrics is poor!" 
"""
# Example 1
string1 = "The lyrics is not that poor!"
a = string1.index("not")
b = string1.index("poor")

if "not" in string1 and "poor" in string1 and a < b:
    a = string1.index("not")
    b = string1.index("poor")
    string1 = str(string1[:a]) + "good"
print(string1)


# Example 2
string2 = "The lyrics is poor!"
y = string2.index("poor")

if "not" in string2 and "poor" in string2 and x < y:
    x = string2.index("not")
    y = string2.index("poor")
    string2 = str(string1[:x]) + "good"
print(string2)









