#1.the tip calculator

#float() use for convert string into number
bill_amount = float(input("Enter your amount :"))
tip_per = float(input("Enter percentage :"))
tip_amount = bill_amount *(tip_per/100)
total_amount = bill_amount + tip_amount
print("your tip amount is :",total_amount)

#2
first_name = input("Enter your name")
last_name = input("Enter your last name")
age = input("Ente your age")
print("your Full Name is",first_name, last_name, "and your age is", age)

#3
age = int(input("Enter your age :"))
if age >=18:
    print("You can access to watch movie ")
else:
    print("You can't access to watch movie")    

#4 The Simple To-Do List
task = ["Sujan" ,"jamuna","muna" , "anju"]
print("print first index" ,task[0])
add_task = input("Enter your new task ")
task.append(add_task)
print(task)

#5 The Mini-Market Checkout
items = ["milk", "bread","egges"]
print("welcome to the shops")
p1 = float(input(f"Enter price for {items[0]}: "))
p2 = float(input(f"Enter price for {items[1]}: "))
p3 = float(input(f"Enter price for {items[2]}: "))
total = p1 + p2 + p3
if total >=500:
    print("You spent a lot today! Total:",total)
else:
    print("Budget friendly! Total:",total)

your_name = input("Enter your name :")
your_address = input("Enter your Address :")
age = int(input("Enter your age :"))
print("my name is ", your_name,"i live at ",your_address, "i am ",age,"year old")
print(f"my name is {your_name} i lived at {your_address} i am {age} year old")

#for loop
f = ["sujan" ,"sudip","suman"]
for i in f:
    print(f"hello {i}")
range 
for i in range(4):
    print(f"print {i}")

#Day 2 Challenge
# The Automated Bill Generator
items = ["banna", "mango","orange","apple"]
total_bill = 0
for i in items:
    price = int(input(f"Enter the price of {i} :"))
    total_bill += price
    print("-" * 10)
    print(f"your total bill is : {total_bill}")
    

prices = [100, 550, 20, 800, 150]
add_price = int(input("Enter "))
prices.append(add_price)
expensive_count = 0
for x in prices:
    if x>500 :
        print(f"{x} expensive ")
        expensive_count +=1
    else:
        print(f"{x} is cheap")
    
    print(f"Total expensive items found: {expensive_count}")
    
#list
    
names = ["sujan", "ram", "manoj", "ram", "hari"]
names.remove("ram")
names[1] = "shyam"
print(names)

numbers = [10, 45, 23, 89, 67, 89, 34]
numbers.sort()
print(numbers[-2])

a = [3, 1, 5]
b = [6, 2, 4]
c = a+b
c.sort(reverse=True)
print(c)

words = ["Python", "is", "fun"]
result = "->".join(words)
print(result)

words = ["apple", "banana", "kiwi", "watermelon"]
a= (max(words,key=len))
b= (min(words,key=len))
print(f"max value: {a}\t {len(a)} (charecter) \n min value:{b} \t {len(b)} (charecter)")

user_input = input("Enter something")
print(user_input.replace("a","").replace("e",""))
input = input("enter")
b = input.lower().replace(" ","")
print(b==b[::-1])

paragraph = "The quick brown fox jumps over the lazy dog. The dog was not that lazy, really."
input_u = input("enter your ")
print(paragraph.lower().count(input_u))
input_user = input("Enter your words")
print(input_user.count("a")+input_user.count("e")+input_user.count("i"))

input_user = input("Enter")
start = input_user.index("(")
end = input_user.index(")")
print(input_user[ :start-1]+input_user[end+1: ])

user_name = input("Enter username")
user_pass = input("Enter your pass")
len_pass = len(user_pass)
print(f"your username : {user_name}\nyour password{len_pass*"*"} ")

user_input = input("enter your input ")
b = user_input.replace("bad","good")
print(b)

user_input = input("user input ")
b = user_input.strip(".")
print(b)

name = input("enter your username :")
domain = input("enter your domain :")
b = name +"@"+ domain
print(f"your gmail: {b}")
# c = b.lower().removesuffix("@gmail.com")
# print(c)
c = b.lower().split("@")
print(f"your username: {c[0]}")

user_input = input("Enter your input: ")
b = user_input.replace(" ","_")
print(f"Final Result : {b}")

#list
Input =" my name is sujan lama"
b = Input.split()
print(len(b))

Input = "Hello World! Python is awesome"
b = Input.split()
c=(Input[::-1])
d = " ".join(c)
print(d)

Input = [4, 5, 1, 4, 2, 3, 8, 9, 11, 55, 0, 9]
b = sorted(Input)
print(b[-2])

Input = "Learning Python is really enjoyable"
b = Input.split()
print(max(b,key=len))

Input = [1, 2, 3, 4]
k = int(input("Enter "))
b = (Input[-k:])
c = (Input[:-k])
print(b+c)
# loops
# while loop
count = 1
while count<=5:
    print("hello sujan",count)
    count  +=1
print(count)

"""print 1 to 100 using while loop"""
i = 1
while i<=100:
    print(i)
    i +=1
print("loops end")

"""print from 100 to 1 using while loop"""
i = 100
while i>=1:
    print(i)
    i -=1

i = 1
n = int(input("Enter you want mul :"))
print(f"Multiplication of {n}........")
while i<=10:
    mul = n*i
    print(f"{n} * {i} = {mul}")
    i +=1

num = [1,4,9,16,25,36,49,64,81,100]
i = 0 
while i<len(num):
    print (num[i])
    i +=1

leap_year = int(input("Enter your year"))

if leap_year%400 ==0:
    print("This is leap year")
else:
    print("This is not leap year")

a = [1,2,3,4,5]
print(a[::-1])
    
a = [1,2,3,4,5]
b =[5,4,3,2,1]
c = []
for i  in range(5):
    c.append(a[i]+b[i]) 
print(c,end=" ")
    

collection = ["sujan", "malayalam","madam",121]
pal = []
for i in collection:
    num = str(i)
    if num ==num[::-1]:
        if num.isdigit():
            pal.append(int(num))
        else:
            pal.append(num)
print(pal)

#Write a function student() that takes:

def student(name,age):
    print(f"your name is {name} and age is {age}")
    
student("sujan lama",23)

'''#Create a function book() with:
title
price
Call the function using keyword arguments.'''

def book(title,price):
    print(f"title of book is {title} and price is {price}")
    
book(title="your dad",price=4000)
'''3. Default Argument
Create a function country() with:
name
country="Nepal"
If country is not given, it should print Nepal.
'''

def country(name, age, country="nepal"):
    print(f'your name is {name} age is {age} and your country name is {country}')

country(name="suman",age=25,country="USA")
country(name="sujan",age=23)

'''4. Positional Arbitrary Argument (*args)
Write a function total() that accepts any number of numbers and prints their sum.'''

def total(*args):
    all =0
    for i in args:
        all+=i
    print(f'total {all}')
    
total(1,2,3,4,5,6)

'''Keyword Arbitrary Argument (**kwargs)
Write a function info() that accepts any keyword arguments and prints them.'''

def info(**kwargs):
    print(kwargs)

info(name="sujan",age=23,location="lalitpur",country="nepal")

'''6. Mixed *args and **kwargs
Create a function data() that:
prints all positional arguments
prints all keyword arguments
'''

def data(*args,**kwargs):
    print(args,kwargs)

data(1,2,34,56,name="sujan",age=23)
'''7. Find Maximum using *args
Write a function largest() that takes multiple numbers using *args and prints the largest number.
'''

def largest(*args):
    print(max(args))
    
largest(2,3,4,6,7,88,45,55,122)

'''Employee Salary using **kwargs
Create a function salary() that accepts:
basic
bonus
overtime
travel
using **kwargs and prints total salary.'''

def salary(**kwargs):
    total =0
    for i in kwargs.values():
        total+=i
    print(f"total is {total}")

salary(basic=20000,bonus=2300,overtime=789,travel=5000)

# # '''10. Combination Practice
# # Write a function:
# # def show(name, *marks, **info):
# # Requirements:
# # print student name
# # print total marks
# # print extra information'''

def show(name, *marks,**info):
    print(f'your name is {name}')
    print(f'from {info}')
    total_marks=0
    for i in marks:
        total_marks+=i
    print(f'your total marks is {total_marks}')
        
    
show('sujan',45,55,66,78,90,city='lalitpur')

'''Bonus Challenge:
Create a calculator function using *args:
calc("+",1,2,3)
calc("*",2,3,4)'''

def calculation(op,*args):
    if op =="+":
        total=sum(args)
        print(total)
    elif op =="*":
        mul=1
        for i in args:
            mul*=i
        print(mul)
            
calculation("+",1,2,3)
calculation("*",2,3,4)

#Print numbers from 1 to 100 using a loop.

for i in range(1,100+1):
    print(i,end=" ")
i =1
while i <=100:
    print(i)
    i+=1

#Find the sum of all even numbers from 1 to 50.

total =0
for i in range(1,100+1):
    if i%2==0:
        total+=i 
print(f'sum of even : {total}')

'''Print a star pattern:
*
**
***
****'''
row= 4

for i in range(1,row+1):
    print("*"*i)

#Reverse a number using a loop
for i in range(10,0,-1):
    print(i)
    
#Count how many digits are in a number.

a=1234
count =0
while a!=0:
    a =a//10
    count+=1
print(count)

#Keep taking input until user types "stop".

while True:
    user_input = input("Enter words :")
    if user_input=="stop":
        break
    print(f'you enterd {user_input}')

#Find factorial of a number using loop.

fact = 1

user_input =int(input("Eneter you want fact :"))
for i in range(1,user_input+1):
    fact*=i
    
print(fact) 

# #Print all prime numbers between 1 and 100.

for i in range(2,100+1):
    is_prime = True
    for num in range(2,i):
        if i%num==0:
            is_prime=False
            break
    if is_prime:
        print(i)

#Find the largest number in a list using loop only.
num =[2,3,5,66,77,34]
lagr =num[0]
for i in num:
    if i>lagr:
        lagr=i
print(lagr)

# Create a function to add two numbers.

def sum(op,*args):
    total = 0
    for i in args:
        if op=="+":
            total+=i
    print(total)

sum("+",1,2,3,4)

#Create a function to check even or odd.

# # # def odd_even(num):
# # #     if num%2==0:
# # #         print(f'your num is even {num}')
# # #     else:
# # #         print(f'your num is odd :{num}')
# # # odd_even(num=int(input("Enter num :")))

# # #Create a function to find factorial.

# # # def factorial(num):
# # #     fact=1
# # #     for i in range(1,num+1):
# # #         fact*=i
# # #     print(f'your fact is {fact}')
# # # factorial(num=int(input("Enter Num :")))

# # #Create a function that returns largest of 3 numbers.

# # # def lasrgest(a,b,c):
# # #     if a>b and a>c:
# # #         print(f' {a} is greater')
# # #     elif b>a and b>c:
# # #         print(f'{b} is greater ')
# # #     else:
# # #         print(f'{c} is greater')

# # # lasrgest(22,3,4)

# # #Create a function to count vowels in a string.

# # # def vowels(word):
# # #     vowel="aeiou"
# # #     count =0
# # #     for ch in word:
# # #         if ch in vowel:
# # #             count+=1
# # #     print(count)

# # # vowels('apple')

# # #Create a function with default argument.
# # # def default_argu(name , age , collage="nesfield"):
# # #     print(name , age ,collage)

# # # default_argu(name='sujan',age=23)

# # #Create a calculator using functions.

# # # def calculator(op,num1,num2):
# # #     if op=="+":
# # #         sum = num1+num2
# # #         print(f'your sum {sum}')
# # #     elif op == "-":
# # #         sub = num1-num2
# # #         print(f'your divi {sub}')
# # #     elif op == "*":
# # #         mul = num1*num2
# # #         print(f'your mul is {mul}')
# # #     elif op == "/":
# # #         if num2==0:
# # #             print("cannot divided by 0")
# # #         else:
# # #             div = num1/num2
# # #             print(f'your div is {div}')
            
# # # op=input("Enter operator +_*/ :")
# # # num1 =int(input("Enter num 1:"))
# # # num2 = int(input("Enter num 2 :"))
# # # calculator(op,num1,num2)

# # #Store student name and marks in a dictionary.

# # # student = {
# # #     'name' : 'sujan',
# # #     'marks' :  {
# # #          'math' : 89,
# # #          'english ' : 90,
# # #          'science' :90
# # #      }
# # # }

# # # print(student['marks']['math'])

# # #Add a new key-value pair in dictionary.

# # # student = {
# # #     'name' : 'sujan',
# # #     'age' :23
# # # }

# # # student['email'] ='sujanlama@gmail.com' #add new key-value pair in dic

# # # print(student)

# # #Update a value in dictionary.
# # # student = {
# # #     'name' : 'sujan',
# # #     'age' :23
# # # }

# # # student['name']='anjan' #update value in dic
# # # print(student)

# # #Delete a key from dictionary.
# # # student = {
# # #     'name' : 'sujan',
# # #     'age' :23
# # # }

# # # del student['name']
# # # print(student)

# # #Print all keys using loop.
# # # data = {
# # #   "coord": {
# # #     "lon": 10.99,
# # #     "lat": 44.34
# # #   },
# # #   "weather": [
# # #     {
# # #       "id": 501,
# # #       "main": "Rain",
# # #       "description": "moderate rain",
# # #       "icon": "10d"
# # #     }
# # #   ],
# # #   "base": "stations",
# # #   "main": {
# # #     "temp": 298.48,
# # #     "feels_like": 298.74,
# # #   },
# # #   "visibility": 10000,
# # #   "wind": {
# # #     "speed": 0.62,
# # #     "deg": 349,
# # #     "gust": 1.18
# # #   }
# # # }
# # # for i in data.keys():
# # #     print(i)

# # #Print all values using loop.

# # # data = {
# # #   "coord": {
# # #     "lon": 10.99,
# # #     "lat": 44.34
# # #   },
# # #   "weather": [
# # #     {
# # #       "id": 501,
# # #       "main": "Rain",
# # #       "description": "moderate rain",
# # #       "icon": "10d"
# # #     }
# # #   ],
# # #   "base": "stations",
# # #   "main": {
# # #     "temp": 298.48,
# # #     "feels_like": 298.74,
# # #   },
# # #   "visibility": 10000,
# # #   "wind": {
# # #     "speed": 0.62,
# # #     "deg": 349,
# # #     "gust": 1.18
# # #   }
# # # }

# # # for i in data.values():
# # #     print(i)

# # #Count frequency of characters in a string.

# # # user_input = input("enter words :")

# # # freq ={}

# # # for i in user_input:
# # #     if i in freq:
# # #         freq[i]+=1
# # #     else:
# # #         freq[i] =1
# # # print(freq)

# # #Merge two dictionaries.
# # # dic1 ={
# # #     'name':'sujan',
# # #     'age' : 23
# # # }
# # # dic2 ={
# # #     'name' :'anjan',
# # #     'age' : 33
# # # }

# # # merg = dic1.copy()

# # # for key,value in dic2.items():
# # #     merg[key]=value
# # # print(merg)

# # # print(len(["hi",1,2,3]))

# # # def show(sujan):
# # #     print('hello sujan !!!')
# # #     def show1():
# # #         print('how are you!!!')
# # #         sujan()
# # #     return show1()       
# # # @show
# # # def student():
# # #     print('my name is what!!!') 
    
# # # student()


# # #oop practice:

# # """4. Student Class
# # Create a class Student.
# # Attributes:
# # name
# # age
# # faculty
# # Method:
# # show() → print all details"""

# # # class Student:
# # #     def __init__(self,name,age,faculty):
# # #         self.name= name
# # #         self.age= age
# # #         self.faculty= faculty
    
# # #     def show(self):
# # #         print(f'My name is {self.name}')
# # #         print(f' my age is {self.age}')
# # #         print(f'Faculty : {self.faculty}')
    
# # # stu=Student(name='sujan',age=23,faculty="Science")
# # # stu.show()  

# # """5. Car Class
# # Create a class Car.
# # Attributes:
# # brand
# # model 
# # speed
# # Methods:
# # start()
# # stop()
# # show_speed()"""

# # # class Car:
# # #     def __init__(self,brand, model,speed):
# # #         self.brand=brand
# # #         self.model=model
# # #         self.speed=speed
    
# # #     def start(self):
# # #         print(f'{self.brand} is stard...')
    
# # #     def show_speed(self):
# # #         print(f'Speed is {self.speed}')
    
# # #     def stop(self):
# # #         print(f'your {self.brand} is stop...')

# # # car=Car(brand='BYD', model='auto2',speed='120')
# # # car.start()
# # # car.show_speed()
# # # car.stop()

# # """. Employee Management System
# # Create class Employee.
# # Attributes:
# # name
# # salary
# # position
# # Methods:
# # yearly_salary()
# # bonus()"""

# # # class Employee:
# # #     def __init__(self,name , salary,position):
# # #         self.name= name
# # #         self.salary = salary
# # #         self.position = position
    
# # #     def yearly_salary(self):
# # #         print(f'Hey {self.name} your yearly salary is {self.salary*12}')
    
# # #     def bonus(self,bonus):
# # #         print(f'hey {self.name} your salary with bonus is {self.salary+bonus}')
        

# # # employee = Employee(name='sujan', salary=90000,position='CEO')
# # # employee.yearly_salary()
# # # employee.bonus(20000)
        
# # """11. Library Management System
# # Create class Book.
# # Attributes:
# # book_name
# # author
# # price
# # Methods:
# # show_book()
# # discount_price()
# # Create multiple book objects."""   
# # class Book:
# #     def __init__(self,title,author):
# #         self.title= title
# #         self.author=author
        
# # class Library:
# #     def __init__(self):
# #         self.books=[]
# #     def add_books(self,book):
# #         self.books.append(book)
# #     def show_books(self):
# #         print(f'library')
        
# #         for book in self.books:
# #             print(f'title : {book.title} and author : {book.author}')
            
# # bookss = Book(title='sujan books',  author='sujan lama')
# # lib = Library()
# # lib.add_books(bookss)
# # lib.show_books()

# from abc import ABC, abstractmethod
# import random


# class Payment(ABC):

#     def __init__(self):
#         self._paid_amount = 0

#     @abstractmethod
#     def pay(self, amount):
#         pass

#     @abstractmethod
#     def refund(self, amount):
#         pass

#     @abstractmethod
#     def get_transaction_id(self):
#         pass

#     def receipt(self, amount):

#         print("\n========= PAYMENT RECEIPT =========")

#         print("Transaction ID :", self.get_transaction_id())

#         print("Amount :", amount)

#         print("===================================")


# class PaymentHistory:

#     history = []

#     @classmethod
#     def add_history(cls, provider, transaction_id, amount, status):

#         cls.history.append({
#             "provider": provider,
#             "transaction_id": transaction_id,
#             "amount": amount,
#             "status": status
#         })

#     @classmethod
#     def show_history(cls):

#         print("\n========= PAYMENT HISTORY =========")

#         for record in cls.history:
#             print(record)


# class Esewa(Payment):

#     def __init__(self):
#         super().__init__()

#         self.__transaction_id = \
#             f"ESW-{random.randint(1000,9999)}"

#     def pay(self, amount):

#         assert amount > 0, \
#             "Amount must be positive"

#         self._paid_amount = amount

#         print(f'Esewa payment successful : Rs {amount}')

#         PaymentHistory.add_history(
#             "Esewa",
#             self.__transaction_id,
#             amount,
#             "Paid"
#         )

#     def refund(self, amount):

#         assert amount <= self._paid_amount, \
#             "Refund amount exceeds payment"

#         print(f'Esewa refund successful : Rs {amount}')

#         PaymentHistory.add_history(
#             "Esewa",
#             self.__transaction_id,
#             amount,
#             "Refund"
#         )

#     def get_transaction_id(self):

#         return self.__transaction_id


# class Khalti(Payment):

#     def __init__(self):
#         super().__init__()

#         self.__transaction_id = \
#             f"KHL-{random.randint(1000,9999)}"

#     def pay(self, amount):

#         assert amount > 0, \
#             "Amount must be positive"

#         self._paid_amount = amount

#         print(f'Khalti payment successful : Rs {amount}')

#         PaymentHistory.add_history(
#             "Khalti",
#             self.__transaction_id,
#             amount,
#             "Paid"
#         )

#     def refund(self, amount):

#         assert amount <= self._paid_amount, \
#             "Refund amount exceeds payment"

#         print(f'Khalti refund successful : Rs {amount}')

#         PaymentHistory.add_history(
#             "Khalti",
#             self.__transaction_id,
#             amount,
#             "Refund"
#         )

#     def get_transaction_id(self):

#         return self.__transaction_id


# class Paypal(Payment):

#     def __init__(self):
#         super().__init__()

#         self.__transaction_id = \
#             f"PPL-{random.randint(1000,9999)}"

#     def pay(self, amount):

#         assert amount > 0, \
#             "Amount must be positive"

#         self._paid_amount = amount

#         print(f'Paypal payment successful : Rs {amount}')

#         PaymentHistory.add_history(
#             "Paypal",
#             self.__transaction_id,
#             amount,
#             "Paid"
#         )

#     def refund(self, amount):

#         assert amount <= self._paid_amount, \
#             "Refund amount exceeds payment"

#         print(f'Paypal refund successful : Rs {amount}')

#         PaymentHistory.add_history(
#             "Paypal",
#             self.__transaction_id,
#             amount,
#             "Refund"
#         )

#     def get_transaction_id(self):

#         return self.__transaction_id


# # Objects
# e1 = Esewa()
# k1 = Khalti()
# p1 = Paypal()


# # Polymorphism
# payments = [e1, k1, p1]

# amounts = [1000, 2000, 3000]

# for provider, amount in zip(payments, amounts):

#     provider.pay(amount)

#     provider.receipt(amount)


# # Refund
# e1.refund(500)


# # Show History
# PaymentHistory.show_history()

class BankAccount():
    def __init__(self,pin,initial_balance=0.0):
        self.__pin = pin
        self.__balance=initial_balance
        
    def deposit(self,amount):
        if amount>0 :
            self.__balance+=amount
            print(f"Your deposite Rs {amount} and total balance Rs {self.__balance}")
        else:
            print(f'Amout cannot be nagative!')
    def withdraw(self,amount,pin):
        if pin==self.__pin:
            if amount<=self.__balance and amount>0 :
                self.__balance -= amount
                print(f"you withdraw Rs {amount} and total Balance Rs {self.__balance}")
            else:
                print('Insufficient balance')
        else:
            print("Incorrect Pin")
        
    def check_balance(self,pin):
        if pin==self.__pin:
            print(f'Total Balance : Rs {self.__balance}')
        else:
            print("Incorrect Pin")
            
    def change_pin(self,old_pin, new_pin):
        if old_pin==self.__pin:
            self.__pin=new_pin
            print(f'pin change sucessful')
        else:
            print(f'Incorrect pin')
        
ob = BankAccount(1234)
ob.deposit(10000)
# ob.withdraw(pin=1243,amount=293)
ob.check_balance(1234)
ob.change_pin(old_pin=1234,new_pin=1111)
ob.check_balance(1111)

            
            
        
a = ['nepal','india','apple']
b = ['sujan', 'rohan','anjan','anju']
print(sorted(b))
