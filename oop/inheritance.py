'''inheritance:  a class that inherit al method and atributes from another class
creating new class from existing class
types :
parent class: base class
child class: derived class

1.single inheritance
2.single level inheritance
3.multiple inheritance
4 heirachical inheritance
5. hybrid'''

#single inheritance 
# class A(): #parent class
#     def show1(self):
#         print('this is feature one')

# class B(A): #child
#     def show2(self):
#         print('this is feature 2')

# ob=B()
# ob.show2()
# ob.show1()

#single level (multi-level)
# class A(self): #grand parent class
#     def show1(self):
#         print('this is feature one')

# class B(A): #parent
#     def show1(self):
#         print('this is feature 2')

# class C(B): #child
#     def show3(self):
#         print('this is feature 3')
        

# ob=C()
# ob.show3()
# ob.show2()
# ob.show1()

#multiple inheritance(mixin)
# class A(): #father
#     def show1():
#         print('this is feature one')

# class B(): #mother
#     def show1(self):
#         print('this is feature 2')

# class C(A,B): #child
#     def show3(self):
#         print('this is feature 3')
        

# ob=C()
# ob.show3()
# ob.show2()
# ob.show1()

#heirachical inheritance
# class A():  #parent 
#     def show1(self):
#         print('this is feature one')

# class B(A): #child1
#     def show1(self):
#         print('this is feature 2')

# class C(A): #child2
#     def show3(self):
#         print('this is feature 3')

# ob=C()
# ob.show3()
# ob.show2()
# ob.show1()