#create a class
class Person:
    name = ""
    weight = 0

#create objects of a class
person1 = Person()
person2 = Person()

# modify the person/weight attributes
person1.name = "Mike"
person1.weight = 45
print(f"Person: {person1.name}, Weight: {person1.weight}")
person2.name = "Wazovski"
person2.weight = 52.3
print(f"Person: {person2.name}, Weight: {person2.weight}")
