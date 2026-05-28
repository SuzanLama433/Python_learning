'''
=====class: it is group of attribute and method==========

1.attribute: it represent variable that contain data
Type of attrible:
a. Instance variable :(those variable whose seperated copy 
   of the file is created  for every object)
   (it help to access instance variable)

b. class variable/ static variable
---> those variable whose single copy of file is created for every object


2.method: it is similar function that perform some task
type of method
a. instance method
b. class method
c. static method
        
'''
# example of instance varibale  (those variable whose seperated copy )
#    of the file is created for every object)
# class Student:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age

#     def show(self): #instance method : it help to access intance variable
#         print(f"my name is{self.name}")

# ob = Student(name='sujan',age=23)
# ob.name = "anjan"
# ob2  = Student(name='rohan',age=22)
# print(ob2.name)
# print(ob.name)  
# ob.show()
# ob2.show()

#class variable : those variable whose single copy of file is created for every object
# class Student:
#     school = "moliss"
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
        
#     @classmethod #it is used acces the class variable
#     def show_school(cls):
#         print(f' my school nama is :{cls.school}')

#     def show(self): 
#         print(f"my name is {self.name} and my school name is {self.school}")
        
# ob = Student(name='sujan',age=23)
# ob.school='janbhawana'
# ob.show_school()
# ob.show()
 
# static method 

# class Student():
#     @staticmethod
#     def show():
#         print("my name us sujan")
        
# ob =Student()
# ob.show()

#6,7,

