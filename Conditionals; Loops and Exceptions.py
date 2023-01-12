#Conditionals - If / Elif / Else


'''x= 11

if x > 5:
    print("x is greater than 5")
    print(x * 2)
elif x == 5:
    print("x is 5")
else:
    print("x is not greater than 5")

if x == 5 and type(x) is int:
    print("x equals 5. x is integer")
    print(x)
elif x == 10 and type(x) is int:
    print("x is an integer, but is not equal to 5")


#Loops - For / For-Else

vendors = ["Cisco", "HP", "Nortel", "Avaya", "Juniper"]
for each_vendor in vendors:
    print(each_vendor)

my_string = "Cisco"
for letter in my_string:
    print(letter)
    print(letter * 2)
    print(letter * 3)

r = range(10)

for i in r:
    print(i * 2)

vendors = ["Cisco", "HP", "Nortel", "Avaya", "Juniper"]
print(len(vendors))
print(list(range(5)))

for element_index in range(len(vendors)):
    print(vendors[element_index])

for index, element in enumerate(vendors):
    print(index, element)

for element in vendors:
    print(element)
else:
    print("The end of the list has been reached")'''

#While / While else loops

'''x = 1
while x <= 10:
    print(x)
    x = x + 1

while x <= 10:
    print(x)
    x = x + 1
else:
    print("x is now greater than 10")'''


#Nesting

'''x = "Cisco"
if "i" in x:
    if len(x) > 3:
        print(x, len(x))

list1 = [4, 5, 6]
list2 = [10, 20, 30]

for i in list1:
    for j in list2:
        print(i * j)
    print(i)'''

'''x = 1

while x <= 10:
    z = 5
    x += 1
    while z <= 10:
        print(z)
        z += 1

for number in range(10):
    if 5 <= number <= 9:
        print(number)'''

#Break/Continue/Pass

#break to interrupt the loops

'''for number in range(10):
    if number == 7:
        break
    print(number)'''

'''for i in list1:
    for j in list2:
        if j == 20:
            break
        print(i * j)
    print("Outside the nested loop

for i in list1:
    for j in list2:
        if j == 20:
            continue
        print(i * j)
    print("Outside the nested loop")

for i in range(10):
    pass

#Exceptions: read the links attached'''

#Try/Except/Else/Finally

for i in range(5):
    try:
        print(i / 0)
    except ZeroDivisionError as e:
        print(e, "--> Division by 0 is not allowed, sorry!")

for i in range(5): #in case the exception is not met
    try:
        print(i / 1)
    except NameError:
        print("You have a name error in your code!")

for i in range(5): #in case the exception is not met,and it continues to print
    try:
        print(i / 1)
    except NameError:
        print("You have a name error in your code!")
    print("The rest of the code..")

#multiple exceptions

for i in range(5):
    try:
        print(i / 1)
    except ZeroDivisionError:
        print("Division by 0 is just wrong!")
    except NameError:
        print("Name error detected!")
    except ValueError:
        print("Wrong value!")

try:
    print(4 / 2)
except NameError:
    print("Name Error!")
else:
    print("No exceptions raised by the try block!")

try:
    print(4 / 2)
except NameError:
    print("Name Error!")
finally:
    print("I don't care, I'm getting printed either way!")

try:
    print(4 / 0)
except NameError:
    print("Name Error!")
finally:
    print("I don't care, I'm getting printed either way!")







