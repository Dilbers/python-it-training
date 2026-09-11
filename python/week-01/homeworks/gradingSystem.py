__author__ = "Muhammed Mahir Varlioglu"
__email__ = "mmahirv@hotmail.com"
#Project: Student Grading System
#Practice dictionaries, lists, loops, and averages.
#Ask the user for at least 3 students.
#Each student gets 3 grades.
#Store in a dictionary:
#students = {
#    "Ali": [80, 90, 70],
#    "Ayşe": [85, 75, 95],
#    "Mehmet": [60, 70, 65]
#}
#Print each student’s average.
#Extra: Show the student with the highest average.

import random


def getThreeRandomGradeList():
    grades = []

    for i in range(3):
        grades.append(random.randint(0, 100))

    return grades

students = {}
studentNames = []
total_grade = 0
highest_avarage = 0
highest_students = []

print("Enter at least 3 student name en press only 'Q' for exit!")

while True:
    student = input("name: ")
    if(len(studentNames) < 3 and student.lower() == 'q'):
        print(f"\033[93m[Warning] Please Enter {3 - len(studentNames)} student more!\033[0m")
    elif(student.lower() == 'q'):
        break
    else:
        studentNames.append(student)

for i in studentNames:
    students[i] = {'grades': getThreeRandomGradeList()} 

for name in studentNames:
    for grade in students[name]['grades']:
        total_grade += grade

    students[name]['avarage_grade'] = total_grade / len(students[name]['grades'])
    total_grade = 0

    print(f"Avarage Grade of {name} is: {int(students[name]['avarage_grade'])}")

    if(highest_avarage < students[name]['avarage_grade']):
        highest_avarage = students[name]['avarage_grade']
        highest_students = []
        highest_students.append(name)
    elif(highest_avarage == students[name]['avarage_grade']):
        highest_students.append(name)

if(len(highest_students) == 1):
    print(f"Highest Grade of student is: {highest_students[0]} en his/her grade: {int(highest_avarage)}")
else:
    students_list = " ".join(highest_students)
    print(f"Highest Grade of students are: {students_list} en their grade: {int(highest_avarage)}")