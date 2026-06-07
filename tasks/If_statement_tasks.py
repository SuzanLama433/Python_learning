"""1. Write a program to input a number from the user and check whether it is even or odd."""

enter_num = int(input("enter your number :"))

if enter_num%2==0:
    print("numbe is even")
else:
    print("num is odd")
    
"""Write a program to check whether a given age is a valid age or not.
Note: A valid age is typically between 0 and 150 (inclusive)."""

age = int(input("Enter your age :"))
if age>0 and age <=150:
    print("valid age")
else:
    print("invalid age")

"""Write a program to input a character and check whether it is a vowel (a, e, i, o, u) or a consonant."""

user_input = input("enter your character :")

if user_input == "a" or user_input == "e" or user_input=="i" or user_input == "o" or user_input=="u":
    print("vowel")
else:
    print("consonant")

vowel = ("a", "e", "i", "o","u") 
your_char = input("Enter your char :")
your_char = your_char.lower()

if your_char in vowel:
    print("vowel")
else:
    print("consonant")

"""Write a program to check if a number entered by the user is divisible by 5 or not."""
user_input = int(input("Enter your num :"))
if user_input%5==0:
    print("divisible by 5")
else:
    print("cannot")

"""Write a program to check whether a string entered by the user is a palindrome (same forward and backward)."""
user_input= input("Enter your word :")
palindrome = user_input.lower()

if palindrome == palindrome[::-1] :
    print("your word is palindrome")
else:
    print("not")    

"""Task 14.
Write a program to input marks and assign grades based on the following conditions:
• 90 and above → Grade A
• 80 and above → Grade B
• 70 and above → Grade C
• 60 and above → Grade D
• Below 60 → Fail"""

user_input = int(input("enter marks :"))
if user_input>0 and user_input<=100:
    if user_input <= 60:
        print("fail")
    elif user_input>60 and user_input<=70:
        print("grade D")
    elif user_input >70 and user_input <= 80:
        print("Grade C")
    elif user_input >80 and user_input<=90:
        print("Grade B")
    else:
        print("Grade A")
else:
    print("enter valid number")

"""Write a program that inputs a student's marks and prints 'Pass' if marks are 40 or more, otherwise prints 'Fail'."""
user_input = int(input("Enter Marks :"))

if user_input>=40:
    print("Your are pass")
else:
    print("you are fail")

"""Write a program to check whether a number lies between 10 and 50 (inclusive)."""
num = int(input("Enter num :"))

if num>10 and num <=50:
    print("your number lies between 10 and 50")
else:
    print("not lies between 10 to 50")
"""Write a program to validate whether an email ends with '@gmail.com'."""
email = input("Enter your email :")
if email.endswith("@gmail.com"):
    print("valid email")
else:
    print("Invalid email")

"""Task 10.
Write a program to input two numbers and print which one is greater. If both are equal, print that they are equal."""

first_num = int(input("Enter first Num :"))
second_num = int(input("Enter second num :"))

if first_num>second_num:
    print("first num is greater")
elif second_num==first_num:
    print("both are equal")
else:
    print("second num is greater")

"""Write a program to input a number and determine whether it is positive, negative, or zero."""
enter_num = int(input("Enter Number :"))
if enter_num<0:
    print("num is neg")
elif enter_num==0:
    print("num is zero")
else:
    print("num is positive")

"""Write a program where if the total shopping bill is greater than 1000, apply a 10% discount and print the final amount"""
enter_amount = int (input("Enter your Amount :"))

if enter_amount>1000:
    dis = enter_amount*.01
    final_bill = enter_amount - dis
    print(f"Your discount is Rs.{dis} and final amount is Rs.{final_bill}")
else:
    print(f"No discount , toal bill Rs.{enter_amount}")

"""Write a Python program to create a simple calculator that takes two numbers (num1 and num2) and an
operator (+, −, ×, ÷) as input from the user. Perform the corresponding operation based on the given operator
using elif statements.
Note: Handle division by zero appropriately."""

enter_first_num = int(input("Enter first Num :"))
enter_second_num = int(input("Enter Second Num :"))
enter_operator = input("Enter operators (+,-,*,/) :")

if enter_operator == "+" :
    print(f"Add: {enter_first_num+enter_second_num} ")
elif enter_operator == "-":
    print(f"Div :{enter_first_num-enter_second_num}")
elif enter_operator == "*":
    print(f"Mul :{enter_first_num*enter_second_num}")
elif enter_operator=="/":
   if  enter_second_num != 0:
     print(f"Div :{enter_first_num/enter_second_num}")
   else:
         print("cannot div by zero") 
else:
    print("Invalid op")

"""Write a program to input three numbers and print the largest among them."""

first_num = int(input("Enter 1st num : "))
second_num = int(input("Enter 2nd num :"))
third_num = int(input("enter 3rd num :"))

if first_num >=second_num and first_num>=third_num:
    print("first num is large : num is ",first_num)
elif second_num>=first_num and second_num>=third_num:
    print("second num is large : num is ",second_num)
else:
    print("3rd num is large : num is ",third_num)
    
"""Write a program to validate a login system. If username is 'admin' and password is '1234', print 'Login
Successful', else print 'Invalid Credentials'."""

print("Login Portal..........")
username = input("enter username :")
password = input("Enter password :")
if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Credentials'")
"""Write a program that takes three sides of a triangle and checks whether the sides can form a valid triangle.
Note: A triangle is valid if the sum of any two sides is greater than the third side."""

first_side= int(input("Enter 1st side :"))
second_side = int(input("enter 2nd side :"))
third_side = int(input("Enter 3rd side :"))

if first_side+second_side>third_side and second_side+third_side> first_side and third_side+first_side>second_side:
    print("valid triangle......")
else:
    print("Invalid Triangle........")

"""Write a program that calculates an electricity bill based on units consumed:
• Units ≤ 100 : Rate = Rs. 5 per unit
• Units 101 – 200 : Rate = Rs. 7 per unit
• Units > 200 : Rate = Rs. 10 per unit"""
enter_units = int(input("Enter Units :"))

if enter_units <=100:
    total_amount = enter_units*5
    print(f"Your total amount : {total_amount}")
elif enter_units>100 and enter_units<=200:
    total_amt = enter_units*7
    print(f"Total Bill :{total_amt}")
elif enter_units >200 :
    total_amt2 = enter_units*10
    print(f"total bill :{total_amt2}")

"""Task 19.
Write a program to check if a student gets a scholarship.
• Scholarship is granted if marks > 85 AND attendance > 75%"""

marks = int(input("Enter marks :"))
attendance = int(input("Enter attendance :"))

if marks>85 and attendance>75:
    print("Scholarship Granted")
else:
    print("Scholarship not Granted")

"""Task 20.
Write a program to input temperature and classify it:
• Above 30°C → Hot
• Between 15°C–30°C → Warm
• Below 15°C → Cold"""
temperature = int(input("Enter temperature °C:"))

if temperature>30:
    print("Hot")
elif temperature>15 and temperature<=30:
    print("warm")
else:
    print("cold")

"""Task 21.
Write a program to check whether a given year is a century year (year ends with 00)."""
year = int(input("Enter a year: "))

if year % 100 == 0:
    print("Century Year")
else:
    print("Not a Century Year")

"""Task 22.
Write a program to give a movie ticket discount:
• Age < 12 or Age > 60 → Discount applies
• Otherwise → No discount"""

print("welcome to bus ticket system.....")
age = int(input("ente your age :"))
if age>0:
    if age <=12:
        print("you are free to travel....")
    elif age>12 and age <= 18:
        print("you have to pay Rs .30")
    elif age > 18 and age <=60:
            print("you have to pay Rs 100")
    elif age >60 and age<= 80:
        print("you have to pay Rs.20")
else:
    print("invalid age")

"""Task 23.
Write a program to determine employee bonus:
• Bonus is awarded only if experience > 2 years AND performance rating > 7"""

experience = int(input("Enter your experience :"))
rating = int(input("Enter your rating :"))

if experience>2 and rating>7:
    print("Bonus Awarded")
else:
    print("No Bonus")

"""Task 24.
Write a program to check whether a given year is a leap year.
• Divisible by 4 → Leap year, UNLESS:
• Divisible by 100 → NOT a leap year, UNLESS:
• Also divisible by 400 → IS a leap year
Note: Example: 2000 and 2400 are leap years; 1900 and 2100 are NOT."""

year = int(input("Enter Year :"))

if (year%4 != 0 and year%100 != 0) or (year%400==0):
    print("leap year....")
else:
    print("no leap")

"""ask 25.
Extended Leap Year Task — Given a year, return True if it is a leap year, otherwise return False, following
the Gregorian calendar rules:
• The year can be evenly divided by 4 → Leap year, unless:
• The year can be evenly divided by 100 → NOT a leap year, unless:
• The year is also evenly divisible by 400 → IS a leap year
Note: Years 2000, 2400 are leap years. Years 1800, 1900, 2100, 2200, 2300, 2500 are NOT leap years."""

year = int(input("Enter Year :"))
is_leap= (year%4 != 0 and year%100 != 0) or (year%400==0)
print(is_leap)

#or
year = int(input("Enter a year: "))

if year % 400 == 0:
    print(True)
elif year % 100 == 0:
    print(False)
elif year % 4 == 0:
    print(True)
else:
    print(False)
