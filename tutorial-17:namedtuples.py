# named tuple is light weight object but more readable
# ref : https://www.youtube.com/watch?v=GfxJYp9_nJA

from collections import namedtuple
# import re

# 1st Example
#==============
# normal tuple for RGB. It is difficult to know which index is for which color
color = (255, 22, 224)
print(color[0])

# We can sort it using dictionary. But in dictory you need to type more for differt RGB combination. key and value
col1 = {'red': 255, 'green': 34, 'blue': 23}
col2 = {'red': 255, 'green': 234, 'blue': 233}

# this can be solved using named tuple
Color = namedtuple('Color', ['red', 'green', 'blue'])
col3 = Color(255, 234, 23)
col4 = Color(red=233, green=245, blue=21)   # we can explicitly mention the color as well
print(col3[0])
print(col3.green)  # easy to call

print(col3)
print(col4)

# 2nd Example
#==============

Student = namedtuple('Student', 'fullname age class_ section')
p = re.compile(r'^[Nn]')
students = []

while(True):
    choice = input("Do you want to enter student details (Yes/No): ")
    if re.search(p, choice):
        break

    student_name = input("Enter student full name: ")
    first = student_name.split(" ")[0]
    student_age = int(input("Enter student age: "))
    student_class = int(input("Enter student class: "))
    student_section = input("Enter student section: ")

    first = Student(student_name, student_age, student_class, student_section)
    students.append(first)

print(students)
