'''
===================Encapsulation=====================
Encapsulation : The process of wrapping data(attribute) and
methods(function associated with class) within a sigle unit.

-> main propose :
.To hide the data or to protected data
.To control the access of data

#To achieve Encapuslation, We use access modifier and proporty decorator(**access modifier)

TYPES of access modifier:
1.⁠ ⁠Public accessor: The attribute and method are accessible outside the class(default)
2.⁠ ⁠Private accessor : The attribute and method are accessible on;y within that class
3.⁠ ⁠protected accessor: The attributes and method are accessible only with in that class and subclass '''

# public accessor 
# class Student:
#     def __init__(self):
#         self.name = "sujan lama"
        
#     def show(self):
#         print(f'my name is {self.name}')
        
# ob = Student()

# class B():
#     def display(self):
#         print(f'my name is {ob.name}')
        
# a = B()
# a.display()
    
#private accessor
# class Student:
#     def __init__(self):
#         self.__name = "sujan lama" #private
        
#     def __show(self): #private
#         print(f'my name is {self.name}')
        
# ob = Student()
# print(ob.__dict__) #it access the private attribute and method 
# print('my name is ',ob._Student__name)

# class B():
#     def display(self):
#         print(f'my name is {ob.__name}') #cannot cal the private attribute from another class
        
# a = B()
# a.display()
    
#protected accessor

# class Student:
#     def __init__(self):
#         self._name = "sujan lama" #protected

#     def _show(self): #protected
#         print(f'my name is {self.name}')
        
# ob = Student()

# class B(Student):
#     def display(self):
#         print(f'my name is {ob._name}') 
        
# a = B()
# a.display()


