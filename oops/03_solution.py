'''
1. Create a Class for Students
Objective: Understand classes, objects, and basic methods.

Write a class Student with the following:

Attributes: name, roll_no, marks.
Methods:
display_details(): Print the student's details.
is_passed(): Check if the student has passed (passing marks >= 40).
Create objects for at least three students, set their attributes, and call their methods.
'''

class Student:
    def __init__(self, name, roll_no, marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks
    
    def display_details(self):
        print("Name: ", self.__name)
        print("Roll number: ", self.__roll_no)
        print("Marks: ", self.__marks)

    def is_passed(self): 
        if(self.__marks >= 40):
            print("You are passed")
        else:
            print("You are failed")
    

student = Student("Sameer", 123, 45)

student.display_details()
student.is_passed()
