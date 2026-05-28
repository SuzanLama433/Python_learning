# # '''Student Basic Class Basic
# # INSTANCE VARIABLES
# # name age roll
# # METHOD
# # display_info()
# # Create 2 student objects and print their details using the display method.'''

# class Student:
#     def __init__(self,name , age , roll):
#         self.name= name
#         self.age=age
#         self.roll = roll
        
#     def display_info(self):
#         print(f'my name is {self.name} , age : {self.age} and roll no : {self.roll}')
        
    
# student= Student(name='sujan lama', age=23,roll=31)
# student.display_info()
        
# # """02 Class Variable — School Name Class Var
# # CLASS VARIABLE
# # school_name
# # INSTANCE VARIABLE
# # name
# # Create multiple student objects and print the shared school name through each object — demonstrating how a class
# # variable is shared across all instances"""

# class School:
#     school_name = 'moliss'
#     def __init__(self,name):
#         self.name=name
        
#     @classmethod 
#     def show(cls):
#         print(f'my school name is {cls.school_name} ')
        
#     def show1(self):
#         print(f'{self.name}, {self.school_name}')
        
    
# school = School(name='sujan')
# school.school_name ='jana bhawana'
# school.show()
        
# # """03 Find Average Marks Methods
# # STORE
# # 3 subject marks per student
# # METHOD
# # average()
# # Create multiple student objects with different marks and print the calculated average for each student."""

# class Average:
#     def __init__(self,math,english,computer):
#         self.math = math
#         self.english = english
#         self.computer = computer
        
#     def average(self):
#         print(f'average : {(self.math+self.english+self.computer)/3}')
        
    
# avg = Average(math=40,english=90,computer=95)
# avg.average()

# # """4 Inheritance — Student Types Inheritance
# # CLASSES
# # Student (parent) ScienceStudent (child)
# # EXTRA ATTRIBUTE IN CHILD
# # lab_marks
# # Show how the child class extends the parent by inheriting existing attributes and adding a new one specific to
# # science students"""

# class Student:
#     def __init__(self, name):
#         self.name = name

#     def subject(self):
#         print(f'{self.name} is a student')


# class ScienceStudent(Student):
#     def __init__(self, name, lab_marks):
#         self.name = name
#         self.lab_marks = lab_marks

#     def science_detail(self):
#         print(f'Lab Marks: {self.lab_marks}')


# student = ScienceStudent('Sujan', 90)

# student.subject()
# student.science_detail()

# # """05 Inheritance — Teacher & Student Inheritance
# # CLASSES
# # Person (parent) Student (child) Teacher (child)
# # PARENT VARIABLES
# # name age
# # EACH CLASS MUST HAVE
# # display()
# # Implement a shared base class and two child classes — each with its own version of the display method showing
# # different output."""
# class Person:
#     def display(self):
#         print('I am a person')


# class Student(Person):
#     def display(self):
#         print('Hello, I am a student')


# class Teacher(Person):
#     def display(self):
#         print('Hello, I am a teacher')

# student = Student()
# teacher = Teacher()

# student.display()
# teacher.display()

# # """08 Library System — Mini Project Project
# # CLASSES
# # Book Library
# # BOOK VARIABLES
# # title author
# # LIBRARY METHODS
# # add_book() show_books()
# # Create multiple book objects, add them to the library, and display the full catalogue — combining all OOP concepts in
# # a real-world scenario."""

# class Book:
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
        
# class Library:
#     def __init__(self):
#         self.books = []
        
#     def add_book(self,book):
#         self.books.append(book)
        
#     def show_book(self):
#         print(f'Library')
        
#         for book in self.books:
#             print(f' title : {book.title} , author : {book.author}')

# book1 = Book("Python Basics", "Sujan") #creat object

# library = Library() #creat library obj

# library.add_book(book1) #add book1 in add_book which inside lib class

# library.show_book()         

# """CLASSES
# Rectangle Circle
# SAME METHOD ON BOTH
# area()
# behavior.
# Both classes must define an area() method. Call the same method on different objects to demonstrate polymorphic"""

# class Rectangle():
#     def __init__(self,length ,breadth):
#         self.length = length
#         self.breadth = breadth
        
#     def area(self):
#         print(f'area is : {self.length*self.breadth}')
# class Circle():
#     def __init__(self,radius):
#         self.radius =radius
        
#     def area(self):
#         print(f'circle area: {3.14115*self.radius**2}')
        
# r = Rectangle(3,4)
# c = Circle(4)

# r.area()
# c.area()

# or 

class Rectangle:
    def __init__(self,length ,breadth):
        self.length = length
        self.breadth = breadth
        
    def area(self):
        print(f'area is : {self.length*self.breadth}')
class Circle:
    def __init__(self,radius):
        self.radius =radius
        
    def area(self):
        print(f'circle area: {3.14115*self.radius**2}')
        
        

def show_area(var):
    var.area()
    
r = Rectangle(3,4)
c = Circle(4)

show_area(r)
show_area(c)


# """CLASSES
# EmailNotification SMSNotification
# SAME METHOD, DIFFERENT BEHAVIOR
# send(message)
# Both notification classes respond to the same send() call but handle it differently — showing runtime polymorphism in
# action."""

# class EmailNotification():
#     def send(self):
#         print('this is Email Notification!!!!')

# class SMSNotification(EmailNotification):
#     def send(self):
#         print('This is SMS Notification!!!!')
#         super().send()
    
# ob = SMSNotification()
# ob.send()

# # or 

# class EmailNotification():
#     def send(self,message):
#         return f'Sending Email... {message}'

# class SMSNotification(EmailNotification):
#     def send(self,message):
#         return f'Sending SMS..... {message}'
    
# em =EmailNotification()
# sms = SMSNotification()

# print(em.send('This is Email'))
# print(sms.send('This is SMS'))

                    
        
        

