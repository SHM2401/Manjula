# -*- coding: utf-8 -*-
"""Challenge 03.2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KkrBpp5llccyoTxjAaOCecUsNADd1dx4
"""

class Student:

  def __init__(self, name, roll_number, cgpa):
   self.name = name
   self.roll_number = roll_number
   self.cgpa = cgpa


def sort_students(student_list):
  # Sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list,
                      key=lambda student: student.cgpa,
                       reverse=True)
  # Syntax - lambda arg:exp
  return sorted_students


# Example Usage:
Students = [
    Student("Hari", "A123", 7.8),
    Student("Srikanth", "A124", 8.9),
    Student("Saumya", "A125", 9.1),
    Student("Mahidhar", "A126", 9.9),
]

sorted_students = sort_students(Students)

# Print the sorted list of students
for student in sorted_students:
   print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
                                  student.roll_number,
                                                        student.cgpa))