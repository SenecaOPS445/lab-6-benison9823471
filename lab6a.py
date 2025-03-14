#!/usr/bin/env python3
# Author ID: 151649225

class Student:
    # Define the name and number when a student object is created
    def __init__(self, name, number):
        self.name = name
        self.number = str(number)  # Ensure number is always a string
        self.courses = {}

    # Return student name and number
    def displayStudent(self):
        return 'Student Name: ' + self.name + '\n' + 'Student Number: ' + self.number

    # Add a new course and grade to students record
    def addGrade(self, course, grade):
        self.courses[course] = grade

    # Calculate the grade point average of all courses and return a string
    def displayGPA(self):
        if not self.courses:  # Handle ZeroDivisionError
            return 'GPA of student ' + self.name + ' is 0.0'
        
        total_grades = sum(self.courses.values())
        if total_grades == 0.0:
            return 'GPA of student ' + self.name + ' is 0.0'
        
        gpa = total_grades / len(self.courses)
        return 'GPA of student ' + self.name + ' is ' + str(gpa)

    # Return a list of courses that the student passed (not a 0.0 grade)
    def displayCourses(self):
        passed_courses = [course for course, grade in self.courses.items() if grade > 0.0]
        return passed_courses

if __name__ == '__main__':
    # Create first student object and add grades for each class
    student1 = Student('John', 13454900)
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    # Create second student object and add grades for each class
    student2 = Student('Jessica', 123456)
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    # Display information for student1 object
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    # Display information for student2 object
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())