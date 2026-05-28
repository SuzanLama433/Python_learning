# """polyomorphism ---> many and morphism -->form
# one thing behave in more way(form)

# it allow same function and method behave differently according to object and data types
# types:
# 1.Duck tyes 
# 2.Compile time polyporphism (method overloading)
# 3.run time pol (method overriding)
# 4.operator overloading
# """
# #Duck types
# class A():
#     def course(self):
#         print('i want to learn python')
    
# class B():
#     print('i want to learn Django')
    

# ob = A()
# op = B()

# def show(var):
#     var.course()
    
# show(ob)

# #method overloading : a class contain soem method with multiple time with different parameter

# class A():
#     def show(self):
#         print('hello sujan')
        
#     def show(self,a,b):
#         print(a+b)
        
        
        
# ob = A(2,3)

# # alternative 
# class A():
#     def show(self, a=0,b=0):
#         print('hello sujan',a+b)

# #method overriding : a class contain same method in both parent class and child class

# class A():
#     def show(self):
#         print('hello sujan')
        
# class B(A):
#     def show(self):
#         print('hello rohan')
#         super().show() #it is special function that used to access from parent class
        
# ob = B()
# ob.show()

#MRO
# class A():
#     def show(self):
#         print('this is class A')
        
# class B(A):
#     def show(self):
#         print('this is class B')
#         super().show()
        
# class C(A):
#     def show(self):
#         print('this is class C')
#         super().show()

# class D(B, C):
#     def show(self): #D ->B->C->A
#         print('this is class D')
#         super().show()
     

# ob = D()
# ob.show()

#operator overloading
# print([1,2,3]+[1,2,3]) ->merge

# class A():
#     def __init__(self,x):
#         self.x=x
#     def __add__(self,other):
#         return self.x+other.y

# class B():
#     def __init__(self,y):
#         self.y=y
        
# a=A(2)
# b=B(3)

# print(a+b)

#dunder function (magic function)

# class A():
#     def __init__(self,name):
#         self.name=name
        
#     def __str__(self):
#         return "welcome " + self.name

# ob = A("sujan")
# b = A('anjan')
# print(b)