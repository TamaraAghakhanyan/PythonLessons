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


class Age:
    birth_year = 0
    current_year = 0

    #method to calculate age
    def calculate_age(self):
        print("Age of person =", self.current_year - self.birth_year)

#create objects of a Age class
age1 = Age()

# assign values to all the attributes
age1.current_year = 2023
age1.birth_year = 1994

# access method inside class
age1.calculate_age()

#Python constructors
class Person:
    #constructor function
    def __int__(self, name = ""):
        self.name = name

person1 = Person()