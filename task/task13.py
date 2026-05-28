"""Write a Python program to create a calculator class. 
Include methods for basic arithmetic operations
"""
class Calculator:
    def __init__(self,op,num1,num2):
        self.op =op
        self.num1=num1
        self.num2=num2
        
    def arthemetic_op(self):
        if self.op=="+":
            print(f'your addition {self.num1+self.num2}')
        elif self.op=="-":
            print(f'your sub {self.num1-self.num2}')
        elif self.op=="*":
            print(f'your mul {self.num1*self.num2}')
        elif self.op=="/":
            if self.num2==0:
                print(f'cannot divided by zero')
            else:
                print(f'your div {self.num1/self.num2}')
        else:
            print("Enter valid operation")
            
ob = Calculator(op="-",num1=23,num2=4).arthemetic_op()

# or 
class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        
    def addition(self):
        print(f'your addition {self.num1+self.num2}')
        
    def sub(self):
        print(f'your addition {self.num1-self.num2}')
    
    def mul(self):
        print(f'your addition {self.num1+self.num2}')
        
    def div(self):
        if self.num2==0:
            print(f'cannot divided by zero')
        else:
            print(f'your div {self.num1/self.num2}')

cal = Calculator(num1=12,num2=2)
cal.addition()
cal.sub()
cal.mul()
cal.div()

"""Write a Python program to create a person class. 
Include attributes like name, country and date of birth. 
Implement a method to determine the person's age"""

class Person:
    def __init__(self,name,country,dob):
        self.name= name
        self.country=country
        self.dob=dob
        
    def final_output(self,current_year):
        print(f'my name is {self.name}')
        print(f'i am from {self.country}')
        print(f'my age is {current_year-self.dob}')

age_calculation=Person(name="sujan lama",country="Nepal",dob=2003).final_output()

'''Bank Account System
Create a class BankAccount with attributes like account_number, owner_name, and balance.
Include methods for:
Depositing money.
Withdrawing money (ensure sufficient balance).
Checking the account balance'''

class BankAccount:

    def __init__(self, account_num, owner_name, balance=100000):
        self.account_num = account_num
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self):
        deposit_amt = int(input("Enter deposit money: Rs "))

        if deposit_amt <= 0:
            print("Enter amount greater than zero.")
        else:
            self.balance += deposit_amt
            print(f"Rs {deposit_amt} credited successfully.")
            print(f"Updated balance: Rs {self.balance}")

    def withdraw(self):
        withdraw_amount = int(input("Enter withdraw amount: Rs "))

        if withdraw_amount <= 0:
            print("Enter amount greater than zero.")

        elif withdraw_amount > self.balance:
            print("Insufficient balance.")

        else:
            self.balance -= withdraw_amount
            print(f"Rs {withdraw_amount} debited successfully.")
            print(f"Remaining balance: Rs {self.balance}")

    def total_balance(self):
        print(f"{self.owner_name} balance is Rs {self.balance}")


# Object creation
pb = BankAccount(11129092, "sujan")

# Method calls
pb.deposit()
pb.withdraw()
pb.total_balance()

'''Rectangle Class

Create a class named Rectangle.

Requirements:
Attributes:
length
breadth
Method:
area() → return area of rectangle
Formula:

Area=length×breadth'''

class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        
    def area(self):
        print(f'Area of Rectangle {self.length*self.breadth}')
        
        
area = Rectangle(length=10,breadth=2).area()
        
'''Employee Class

Create a class named Employee.

Requirements:
Attributes:
name
salary
Method:
annual_salary() → calculate yearly salary
Formula:

Annual Salary=Monthly Salary×12'''

class Employee:
    def __init__(self, name , salary):
        self.name=name
        self.salary=salary
        
    def annual_salary(self):
        print(f'{self.name} your annual_salary Rs {self.salary*12}')
    

annual_salary = Employee(name="Sujan",salary=50000).annual_salary()
        
            
            

        
