#Conditionals - If / Elif / Else


x= 11

"""if x > 5:
    print("x is greater than 5")
    print(x * 2)
elif x == 5:
    print("x is 5")
else:
    print("x is not greater than 5")"""

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
    print("The end of the list has been reached")