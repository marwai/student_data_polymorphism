# Same idea, different behaviour
# Imports everything (*) from student_data
from student_data import *

# The subclass devops has student as its base class
class Devops(Student): # The class inherits all the characteristics from student_data
    def __init__(self, name, age, course, skills):
        super().__init__(name, age, course)
        self.skills = skills # unique to devops only


    def new_skill(self): # method is unique to Person
        self.details()
        print("You have learned " + self.skills, "at Sparta global\n")

# instance of method has been named
Marcus = Devops("Marcus", "23" , "Aerospace Engineering", "SQL\n") #\n creates a new line

#Recalls the instance of the class
Marcus.new_skill()


bob =  Devops("bob", "25", "Computer Science", "SQL, Python and AWS\n")
bob.new_skill()

