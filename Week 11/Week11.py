#Problem 1
'''
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
student2 = Student('Bob', 'CIS')


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
    def __str__(self):
        return f'Course Number = {self.course_number}, Course Name = {self.course_name}'
course1 = Course('Programming', 'CIS221')
course1.add_student(student1)
course1.add_student(student2)
course1.show_student_enrollment()
print(course1)
'''
#Problem 9
'''
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
    def set_price(self, value):
        self.price = value
    def show_description(self):
        return f'{self.name} is delicious and cost ${self.price}'
    def __str__(self):
        return f'Item = {self.name}, Price = ${self.price}'

item1 = MenuItem('Pizza', 3)
item2 = MenuItem('Steak', 30)

class Restaurant:
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
        self.menu_items = []
    def add_menu_item(self, menu_item):
        self.menu_items.append(menu_item)
    def display_menu(self):
        for item in self.menu_items:
            print(item.get_name(), item.get_price())
    def __str__(self):
        return f'Welcome to {self.restaurant_name}!'
    def lunch_menu(self):
        for item in self.menu_items:
            normal_price = item.get_price()
            lunch_price = normal_price - 2
            item.set_price(lunch_price)
        self.display_menu()

restaurant1 = Restaurant('Good Shop')
restaurant1.add_menu_item(item1)
restaurant1.add_menu_item(item2)
restaurant1.display_menu()
restaurant1.lunch_menu()
'''
#Problem 10
'''
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def get_author(self):
        return self.author
    def set_author(self, value):
        self.author = value
    def display_info(self):
        return f'{self.title} is written by {self.author}'

class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def display_catalog(self):
        for book in self.books:
            print(book.display_info())

book1 = Book('Good Book', 'Bob')
book2 = Book('Bad Book', 'Fred')
library1 = Library('Awesome Library')
library1.add_book(book1)
library1.add_book(book2)
library1.display_catalog()
'''