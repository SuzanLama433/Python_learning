# """Design and implement a secure BankAccount class that models a real-world bank account using
# Python's data-hiding and encapsulation principles. Your implementation must prevent direct external
# access to sensitive financial data.
# Private Attributes (must use name mangling):
# • __balance — stores the current account balance (float)
# • __pin — stores the 4-digit security PIN (integer)
# Required Methods:
# • __init__(pin, initial_balance=0) — constructor to initialise account
# • deposit(amount) — add a valid positive amount to balance
# • withdraw(amount, pin) — deduct amount after PIN verification
# • check_balance(pin) — return balance only if PIN matches
# • change_pin(old_pin, new_pin) — allow secure PIN change"""

class BankAccount():
    print(f'=====Bank System======')
    def __init__(self, pin , initial_balance=0.0):
        assert initial_balance>=0 ,f'{initial_balance} cannot be negative'
        assert len(str(pin)) == 4 , f'pin must be 4 digits'
        
        self.__pin = pin
        self.__balance =initial_balance
        
    def deposit(self,amount):
        assert amount> 0 ,f'{amount} cannot be negative'
        self.__balance +=amount
        print(f'your deposite Rs {amount} and total balance is {self.__balance}')
        
    def withdraw(self,amount , pin):
        assert pin ==self.__pin , f'{pin} is incorrect'
        assert amount > 0, "Amount must be positive"
        assert amount <= self.__balance, "Insufficient balance"
        
        self.__balance-=amount
        
        print(f'you withdraw amout Rs {amount} and total balance is {self.__balance}')
        
    def check_balance(self,pin):
        assert pin ==self.__pin ,f'{pin} is incorect'  
        print(f'your total balance Rs {self.__balance}')
        
    
    def change_pin(self,old_pin, new_pin):
        assert old_pin ==self.__pin
        assert len(str(new_pin)) == 4, "New PIN must be 4 digits" 

        self.__pin = new_pin
        print(f'your pin change successfuly!!!')        
        
        
        

ob = BankAccount(1234)
ob.deposit(10000)
ob.withdraw(500,1234)
ob.check_balance(1234)
ob.change_pin(1234,1111)
ob.check_balance(1111)  
        
# """Task 2 Student Result Management System
# Build a Student class that manages academic records securely. The system should control how marks
# and attendance data are stored and retrieved, enforcing data-integrity rules at the class level.
# Private Attributes:
# • __marks — dictionary mapping subject names to scores (0–100)
# • __attendance — percentage value (0.0 to 100.0)
# • __name — student's full name
# • __roll_no — unique roll number
# Required Methods:
# • set_marks(subject, score) — set score; reject negative values and scores above 100
# • get_marks(subject) — return mark for a given subject
# • set_attendance(percentage) — set attendance; must be between 0 and 100
# • get_attendance() — return current attendance percentage
# • get_result() — print a formatted result card showing all subjects, scores, and pass/fail status
# • get_gpa() — calculate and return GPA on a 4.0 scale"""

class Student():

    def __init__(self, name, roll_no):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = {}
        self.__attendance = 0.0

    def set_marks(self, subject, score):
        assert 0 <= score <= 100, 'marks must be between 0 to 100'

        self.__marks[subject] = score
        print("Marks added successfully")

    def get_marks(self, subject):

        return self.__marks.get(subject, "subject not found")

    def set_attendance(self, percentage):

        assert 0 <= percentage <= 100, \
            'percentage must be between 0 to 100'

        self.__attendance = percentage

        print('Attendance added successfully!!')

    def get_attendance(self):

        return self.__attendance

    def get_gpa(self):

        if not self.__marks:
            return 0

        total = 0

        for score in self.__marks.values():

            if score >= 90:
                total += 4.0

            elif score >= 80:
                total += 3.5

            elif score >= 70:
                total += 3.0

            elif score >= 60:
                total += 2.5

            elif score >= 50:
                total += 2.0

            elif score >= 40:
                total += 1.0

            else:
                total += 0.0

        return round(total / len(self.__marks), 2)

    def get_result(self):

        print("\n========= RESULT CARD =========")

        print(f"Name       : {self.__name}")
        print(f"Roll No    : {self.__roll_no}")
        print(f"Attendance : {self.__attendance}%")

        if self.__attendance < 75:
            print("Not Eligible for Exam")
            return

        failed = False

        print("\nSubjects:")

        for subject, score in self.__marks.items():

            status = "Pass" if score >= 40 else "Fail" 

            if score < 40:
                failed = True

            print(f'{subject} : {score} ==> {status}')

        print(f'\nFinal Result : {"FAIL" if failed else "PASS"}')

        print("GPA :", self.get_gpa())


s1 = Student("Sujan Lama", 1)

s1.set_marks("Math", 90)
s1.set_marks("Science", 75)
s1.set_marks("English", 95)

s1.set_attendance(80)

print(s1.get_marks("Math"))

print("Attendance:", s1.get_attendance())

s1.get_result()

"""Using Python's abc module, design an abstract base class hierarchy for a vehicle management system.
The structure must enforce a common interface across all vehicle types while allowing each subclass to
provide its own specific implementation.
Abstract Base Class — Vehicle (import from abc module):
• Abstract method: start() — defines how the vehicle starts
• Abstract method: stop() — defines how the vehicle stops
• Abstract method: fuel_type() — returns the type of fuel used
• Concrete method: description() — prints brand and model (set in constructor)
Concrete Child Classes (must implement ALL abstract methods):
• Car — four-wheel vehicle; start() uses an ignition key; fuel: Petrol/Diesel
• Bike — two-wheel vehicle; start() uses a kick/electric start; fuel: Petrol
• ElectricScooter — two-wheel vehicle; start() uses a button; fuel: Electric
Additional Requirements:
• Attempting to instantiate the abstract Vehicle class must raise a TypeError.
• Each child class must have at least one unique attribute (e.g., Car has num_doors).
• Demonstrate polymorphism by storing all vehicles in a list and calling start() on each."""


from abc import abstractmethod ,ABC
class Vehicle(ABC):
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
    @abstractmethod
    def fuel_type(self):
        pass
    
    def description(self):
        print(f'Brand : {self.brand}')
        print(f'model : {self.model}')
        
class Car(Vehicle):
    def __init__(self, brand, model,num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors
    def start(self):
        print(f' {self.brand} car is start!!!!')
    
    def stop(self):
        print(f'{self.brand} is stop!!!')
    
    def fuel_type(self):
        return 'Diesel'        
        
class Bike(Vehicle):
    def __init__(self, brand, model,helmet_types):
        super().__init__(brand, model)
        self.helmet_types =helmet_types
        
    def start(self):
        print(f'{self.brand} bike is start!!!')
    def stop(self):
        print(f'{self.brand} bike is stop!!!')
        
    def fuel_type(self):
        return "petrol"
    
class ElectricScooter(Vehicle):
    def __init__(self, brand, model,battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
    def start(self):
        print(f'{self.brand} ElectricScooter is start ')
    def stop(self):
        print(f'{self.brand} ElectricScooter is stop!!')
    def fuel_type(self):
        return "battery"
    
    
c1 = Car("Toyota", "Corolla", 4)
b1 = Bike("Yamaha", "R15", "Full Face")
e1 = ElectricScooter("Ather", "450X", "3.7 kWh")

vehicles = [c1, b1, e1]
for vehicle in vehicles:
    print(f'=================')
    vehicle.description()
    vehicle.start()
    print(f'Fuel Types : {vehicle.fuel_type()}')
    vehicle.stop()


"""Design a Payment abstract base class that acts as a common interface for multiple real-world payment
providers. Each provider must implement the required methods while potentially adding provider-specific
behaviour.
Abstract Base Class — Payment:
• Abstract method: pay(amount) — process a payment of the given amount
• Abstract method: refund(amount) — process a refund of the given amount
• Abstract method: get_transaction_id() — return a unique transaction identifier
• Concrete method: receipt(amount) — print a formatted payment receipt
Required Child Classes (one per payment provider):
• Esewa — implement pay(), refund(), and generate transaction IDs prefixed with 'ESW-'
• Khalti — implement pay(), refund(), and generate transaction IDs prefixed with 'KHL-'
• Paypal — implement pay(), refund(), and generate transaction IDs prefixed with 'PPL-'
Additional Requirements:
• Each pay() must validate that the amount is positive.
• refund() must check that the refund amount does not exceed the original payment.
• Show runtime polymorphism: process payments from a mixed list of provider objects.
• Add a PaymentHistory class that records all transactions across providers.
Key OOP Concepts:
Abstraction,
Real-World
Interface ,Polymorphism ,Common Interface ,Encapsulation"""
from abc import abstractmethod , ABC
import random
class Payment(ABC):
    def __init__(self):
        self._paid_amount = 0
    
    @abstractmethod
    def pay(self,amount):
        pass
    @abstractmethod
    def refund(self,amount):
        pass
    @abstractmethod
    def get_transaction_id(self):
        pass
    
    def receipt(self,amount):
        print(f'============Payment Receipt========')
        print("transection ID", self.get_transaction_id())
        print("Amount ", amount)
        print("=====================================")
        
        

class PaymetHistory:
    history = []
    
    @classmethod
    def add_history(cls,provider, transaction_id, amount, status):
        cls.history.append({
            "provider ":provider,
            "transaction_id " : transaction_id,
            "amount" :amount,
            "status" :status
        })
        
    @classmethod
    def show_history(cls):
        print("=========Paymet History==========")
        for record in cls.history:
            print(record)    

class Esewa(Payment):
    def __init__(self):
        super().__init__()
        self.__transaction_id = f"ESW-{random.randint(1000,9999)}"
        
    def pay(self, amount):
        assert amount>0 , f'Amount must be positive'
        self._paid_amount = amount
        print(f'Esewa payment sucessfully :Rs {amount}')
        
        PaymetHistory.add_history("Esewa" ,self.__transaction_id,amount,"paid")
        
    def refund(self, amount):
        assert amount<=self._paid_amount ,f'Refund amount exceeds payment'
        print(f'Esewa refun Sucessfuly : Rs {amount}')
        PaymetHistory.add_history("Esewa",self.__transaction_id ,amount,"Refund")
        
    def get_transaction_id(self):
        return self.__transaction_id
    
class Khalti(Payment):
    def __init__(self):
        super().__init__()
        self.__transaction_id = f'KHL-{random.randint(1000,9999)}'
    def pay(self, amount):
        assert amount>0 , f'Amount must be positive'
        self._paid_amount = amount
        print(f'Khatli payment sucessfully Rs {amount}')
        
        PaymetHistory.add_history("Khalti" ,self.__transaction_id,amount,"paid")
    def refund(self, amount):
        assert amount<=self.__paid_amount, f"Refund amount exceeds payment"
        print(f"Khalti refund sucessfully Rs{amount}")
        PaymetHistory.add_history("Khalti",self.__transaction_id,amount,"refund")
    def get_transaction_id(self):
        return self.__transaction_id
    
class Paypal(Payment):
    def __init__(self):
        super().__init__()
        self.__transaction_id = f'PPL-{random.randint(1000,9999)}'
    def pay(self, amount):
        assert amount>0 ,f"amount must be positive"
        self._paid_amount=amount
        print(f'Paypal Payment successful Rs {amount}')
        PaymetHistory.add_history("Paypal",self.__transaction_id,amount,"Paid")
    def refund(self, amount):
        assert amount<=self.__paid_amount,"Refunf amount exceed payment"
        print(f"Paypal refund successful Rs {amount}")
        PaymetHistory.add_history("Paypal",self.__transaction_id,amount,"refund")
        
    def get_transaction_id(self):
        return self.__transaction_id
    
e1 = Esewa()
k1 = Khalti()
p1 = Paypal()
e1.pay(1000)
payments = [e1, k1, p1]

amounts = [1000, 2000, 3000]

for provider, amount in zip(payments, amounts):

    provider.pay(amount)
    provider.receipt(amount)

e1.refund(500) 


PaymetHistory.show_history()

"""Demonstrate Python's multiple inheritance by combining attributes from two independent base classes into
a single derived class. Pay attention to the Method Resolution Order (MRO) and constructor chaining.
Base Class 1 — Employee:
• Attribute: name — employee's full name (string)
• Attribute: employee_id — unique staff identifier (string/int)
• Method: get_employee_info() — returns a formatted employee details string
Base Class 2 — Company:
• Attribute: company_name — name of the organisation (string)
• Attribute: location — city/country of the office (string)
• Method: get_company_info() — returns a formatted company details string
Derived Class — Manager (inherits from Employee AND Company):
• Additional attribute: department — the team the manager leads
• Additional attribute: team_size — number of direct reports (integer)
• Method: show_manager_info() — displays all details from both parent classes plus department
and team size
• Method: promote(new_department) — updates the manager's department
Additional Requirements:
• Use super() properly to call parent constructors.
• Print and explain the MRO using Manager.__mro__.
• Create at least two Manager instances with different company and department details.
Key OOP Concepts:
Multiple Inheritance MRO super()
Constructor
Chaining Derived Classes"""

class Employee:
    def __init__(self,name,employee_id,**kwargs):
        super().__init__(**kwargs)
        self.name=name
        self.employee_id = employee_id
    def get_emplyoee_info(self):
        return f'Emplyoee name: {self.name}\n Employee ID : {self.employee_id}'
    
class Company:
    def __init__(self,company_name,location,**kwargs):
        super().__init__(**kwargs)
        self.company_name= company_name
        self.location = location
    def get_company_info(self):
        print(f'Company Name : {self.company_name}\n Location : {self.location}')

class Manager(Employee,Company):
    def __init__(self, name, employee_id,company_name, location, department, team_size):
        super().__init__(name=name,employee_id=employee_id,company_name=company_name,location=location)
        self.department = department
        self.team_size=team_size
        
    def show_manager_info(self):
        print("======Manager Info========")
        print(self.get_emplyoee_info)
        print(self.get_company_info)
        print(f'Department : {self.department}')
        print(f'Team Size : {self.team_size}')
        
    def promote(self,new_department):
        self.department = new_department
        print(f'{self.name} promoted from {self.department} to {new_department}')


#create object fro manager 1
manager1 = Manager(name="sujan lama",
                   employee_id=1,company_name="Teach Nepal",location="lalitpur",department="Software Development",team_size=10)

#create object fro manager 2
manager2 = Manager(name="sudip lama",
                   employee_id=1,company_name="Teach Nepal",location="kathmadu",department="Software Development",team_size=15)

#display Info for manager1
manager1.show_manager_info()
print("=======================")

#display Info for manager2
manager2.show_manager_info()
print("=======================")

#here i promote manager 1 from Tech Nepal to Ai rech
manager1.promote("AI Research")

#display updated info 
print("\n Updated Info")
manager1.show_manager_info()

#MRO
print("\n===== MRO of Manager Class =====")
for cls in Manager.__mro__:
    print(cls)

        
        

