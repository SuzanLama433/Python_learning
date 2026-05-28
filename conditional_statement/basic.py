"""Conditional Statement :
making decision based on variable hold or result
if statement 
if else
nested

if statement:
syntax:
if condition(true|false):
    block of code
else:
    false_message
"""
# weather = "sunny"
# if weather == "sunny":
#     print("you can take an umbrella")

# price = int(input("enter price"))
# if price>=20:
#     print("i can go coffiee shop")
# else:
#     print("I cannot go")

# age = int(input("Enter your age"))
# if age >=20:
#     print("You are eligible to vote")
# else:
#     print("you cannot ")

#one line statement 
# age = 20
# if age >= 18:print("you can vote")

#shorthandded if statement (ternary op)
#syntax: true_block if condition else false_code
# age = 20
# print("you can vote") if age>=18  else  print("you cannot")

"""
elif:
syntax:
if condition:
   code:
elif condition:
   code:
elif condition:
    code:
else:
    false condition
nested if condition
"""
try :
 print("welcome to bus ticket system.....")
 age = int(input("ente your age :"))
 if age>0:
    if age <=12:
        print("you are free to travel....")
    elif age>12 and age <= 18:
        print("you have to pay Rs .30")
    elif age > 18 and age <=60:
        if age == 30:
            print("You have to free....")
        else:
            print("you have to pay Rs 100")
    elif age >60 and age<= 80:
        print("you have to pay Rs.50")
    else:
        print("you have to free")
 else:
    print("invalid age")
except KeyboardInterrupt :
    print("program stop by user")
finally :
    print("==================================================")
    print("excution finished")
    

    