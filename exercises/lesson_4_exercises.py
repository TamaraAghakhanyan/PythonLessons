"""
Exercise 1:
Print "Hello World" if a is greater than b.
"""
a = 50
b = 10

if a > b:
    print("Hello World")

"""
Exercise 2:
Print "Yes" if a is equal to b, otherwise print "No".
"""
a = 50
b = 10

if a > b:
    print("Hello World")
else:
    print("No")

"""
Exercise 3:
Print "Hello" if a is equal to b, and c is equal to d.
"""
a = 10
b = 10
c = 20
d = 20

if a == b and c == d:
    print("Hello")

"""
Exercise 4: 
Define 4 types of variables if type int, float, string and boolean with some values.
Then define an empty list. Check all variables and 
1. if the variable is type of int and its value 
is greater than 100, then append that var to list.
2. if the var is type of str and its length is not greater than the int var
append the var to list.
3. if the var is boolean print "This are num vars: int: "PUT THE INT VAR VALUE HERE", float: "PUT THE FLOAT VAR VALUE HERE", 
"""

a = int(700)
b = float(101.2)
c = str("Barev")
d = bool(True)
x = []

if type(a) is int and a > 100:
    x.append(a)

if type(c) is str and len(c) <= a:
    x.append(c)
    print(x)

if type(d) is bool:
    print("This are num vars: ")


"""
Exercise 5: 
Ask for 2 integer variables a and b from the user with input function.
Check 3 conditions.
If a value is greater than b print about that.
If a is aqual to b, print about that.
If a is less than b, print about that. 
"""

a = int(input("Enter 1st int: "))
b = int(input("Enter 2nd int: "))

if a > b:
    print(a, "is greater than", b)
elif a == b:
    print(a, "is equal to", b)
elif a < b:
    print(a, "is less than", b)