#1. Print first 10 natural numbers using while loop
'''x = 1
while x <= 10:
    print(x)
    x = x + 1'''


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


'''Write a program to count the total number of digits in a number using a while loop.
For example, the number is 75869, so the output should be 5.

n = int(input("Enter number: "))

count = 0
while n > 0:
    count = count + 1
    n = n // 10
print("The number of digits in the number are:", count)'''


#Exercise 8. print list in reversed order
'''list = [10, 20, 30, 40, 50]

a = list[::-1]

for i in a:
    print(i)'''


#Exercise 9.Display numbers from -10 to -1 using for loop

'''start = -10
end = 0

for i in range(start,end,1):
    print(i)'''

#Exercise 10: Use else block to display a message “Done” after successful execution of for loop

'''n = int(input("Enter Number: "))

for i in range(n):
    if i == n - 1:
       print(i)
       print("Done!")
    else:
        print(i)'''


#Exercise 11: Write a program to display all prime numbers within a range


# find factor of number
'''num = int(input('Enter number: '))

print('The factors of', num, 'are:')
for i in range(1, num+1):
    if(num % i) == 0:
        print(i, end=' ')

a = int(input("Enter 1st Number: "))
n = int(input("Enter the last Number: "))

print("Prime numbers between", a, "and", n, "are:")
for num in range(a, n + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

#Exercise 12: Display Fibonacci series up to 10 terms

num1 = 0
num2 = 1
result = 0

for i in range(10): # run loop 10 times
    print(num1, end=" ") # print next number of a series
    result = num1 + num2 # add last two numbers to get next number

    num1 = num2  # update values
    num2 = result'''





















