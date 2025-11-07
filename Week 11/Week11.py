#Problem 1

class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major
    def get_name(self):
        return self.name
    def set_name(self, value):
        self.name = value
    def get_major(self):
        return self.major
    def set_major(self, value):
        self.major = value
    def __str__(self):
        return f"Hi my name is {self.name} and I am studying {self.major}."

student1 = Student('Brenden', 'CIT')

class Course:
    def __init__(self, course_name, course_number):
        self.course_name = course_name
        self.course_number = course_number
        self.students = []
    def get_number(self):
        return self.course_number
    def set_number(self, value):
        self.course_number = value
    def add_student(self, student):
        self.students.append(student)
    def show_student_enrollment(self):
        for student in self.students:
            print(student.get_name())
    def 
course1 = Course('Programming', 'CIS221')
course1.add_student(student1)
course1.show_student_enrollment()