'''condition: making decision
loop: replace(again and again)
function: reuse(write code one time , use multiple)

oop: it organize code in real world

Programming paradigms: the preocess of solving problem
1.procedureral programming : top ---->down
eg : variable , if , loop , function

2.function programming
print(list(filte(lambda x : x %2==0,a)))

3.declarative programming : it focus on what to achive not how()
list comprehension [i for i in aif condition]

4.OOP ; real world modeling
it organize code in class and object 
--- it map in real world entities 


car 
data(artibute): speed , model , color
feature(method) : break , start , stop

python use class and object to represent oop
class : blueprint of object , template of creating object 
object : instance of class

class: it is group of attribute and method
atribute : it is represent variable that contain data
method : it is similar to function that preform some task

# syntax
class ClassName:
     block of code
    
ob = ClassName()
ob2 = ClassName()
'''
  
#     def show(self):
#         print(f"hello this is {self.name} ")

# class Student:
#     def __init__(self):
#         self.name = "sujan"
#         self.age = 23
        
#     def show(self):
#         print(f"hello this is {self.name} ")
        
# ob = Student().show()
# # or 
# ob.show()

# class Student:
#     def __init__(self,name, age): #init is special method used to initilize the value on variable || self is keyword ,current class or object pointed
#         self.name = name
#         self.age = age
           
#     def show(self):
#         print(f"hello this is {self.name} ")
#         print(f'my age is {self.age}')
        
# ob = Student(name='sujan',age=23).show()
# ob1 = Student(name="rohan",age=23).show()


#shop
#class :shop
#attributes : product_name , price , quantity
#method : total_price
# class Shop:
   
#     def __init__(self,product_name,price,quantity):
#         assert price>0 ,f'{price} cannot be negative'
#         assert quantity>0,f"{quantity} can not be nagative"
#         self.product_name = product_name
#         self.price = price
#         self.quantity =quantity
    
#     def total_price(self,discount):
#         print(f'your product name is {self.product_name} and total price {self.price*self.quantity-discount}')


# book = Shop(product_name="book",quantity=10,price=1000)
# book.total_price(discount=150)
        
'''class: circle
attribute: radius
method : area,perimeter'''

# class Circle:

#     def __init__(self,radius):
#         self.radius = radius
        
#     def area(self):
#         print(f'circle area : {3.1415*self.radius**2}')
    
#     def perimeter(self):
#         print(f'circle perimeter :{2*3.1415*self.radius} ')
        
# ob = Circle(radius=14)
# ob.area()
# ob.perimeter()


#every time create object ,it store in different heap memory location -->instance variable
        