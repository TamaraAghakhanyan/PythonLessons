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
        print(i)'''




