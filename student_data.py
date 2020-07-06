# The super class, Student is the class that other classes inherits from
class Student:
    # method (behaviour) initialises the variables
    def __init__(self, name, age, course): # (name, age, course attributes are defined)
        self.name = name
        self.__age = age
        self.course = course

    # Details of the student
    def details(self):
        # basic print functions
        print("Name: " + self.name)
        print("Age: " + self.__age)
        print("University course: " + self.course)

# Adds the strings together
a = "hel"
b = "lo"
print(a+b) # concatenation of the string

# Adds the numbers together
a = 5
b = 6
print(a+6) # built in python example of polymorphism