""" Task 1: Bank Compound Interest Calculator
A bank offers compound interest on deposits. You need to calculate how much interest and total amount a
customer will receive after the investment period.
1. Calculate the compound amount A using the formula above.
2. Calculate the interest earned (Interest = A - P).
3. Display both values rounded to 2 decimal places."""

Principal =float(input("Enter amout :"))
Annual_Interest_Rate = float(input("Enter rate :"))
Time_t = int(input("Enter time :"))
Compounding_Frequency = int(input("Enter frequency :"))
A = Principal*(1+(Annual_Interest_Rate/100)/Compounding_Frequency)**(Compounding_Frequency*Time_t)
Interest = A -Principal
print(f"Compund Ammount : {round(A,2)}")
print(f'Interest :{round(Interest,2)}')

"""Task 2: Online Shopping Cart Bill Calculator
An e-commerce platform wants to calculate the final bill of a customer including applicable taxes
Given Data
cart = [499, 1299, 349, 199]
VAT Rate = 13%
■ Your Tasks
1. Calculate the total cart amount using a built-in function.
2. Calculate the tax amount (13% VAT on total).
3. Calculate the grand total (subtotal + tax).
4. Display the final payable amount.
"""
cart = [499, 1299, 349, 199]
VAT_Rate = 13/100
cart = list(cart)
total_cart_amount = sum(cart)
tax_amount = total_cart_amount*VAT_Rate
grand_total = total_cart_amount+tax_amount
print(f"Total cart Amount :{total_cart_amount}")
print(f"Tax Amount :{tax_amount}")
print(f"Grand Amount :{grand_total}")

"""■ Task 3: Social Media Engagement Analyzer
 Scenario
A content creator wants to analyze which post performs best based on the number of likes received.
■ Given Data
post_likes = { "post1": 120, "post2": 250, "post3": 90 }
■ Your Tasks
1. Find the most liked post value using a built-in function.
2. Find the least liked post value using a built-in function.
3. Display both results clearly"""

post_likes = { "post1": 120, 
              "post2": 250, 
              "post3": 90 
              }
print(f"Most likes :{max(post_likes,key=post_likes.get)} {max(post_likes.values())}")
print(f"leasr Likes :{min(post_likes,key=post_likes.get)} {min(post_likes.values())}")

"""■ Task 4: Movie Ticket Booking System
Scenario
A cinema wants to calculate the total price for a group ticket booking with a promotional discount applied.
■ Your Tasks
1. Calculate the total ticket cost (price × quantity).
2. Calculate the discount amount (10% of total).
3. Calculate the final payable amount (total − discount).
4. Display the final price clearly."""

ticket_price = float(input("Enter price :"))
num_of_ticket = int(input("Enter number of ticket :"))
discount = int(input("Enter  Discount%"))
dis_cal = discount/100
total_ticket_cost = ticket_price*num_of_ticket
dis_amount = total_ticket_cost*dis_cal
final_payable_amount = int(total_ticket_cost - dis_amount)

print(f"Final Price :{final_payable_amount}")

"""Task A: Time Conversion
Scenario
■ Given Data
Convert a given number of seconds into minutes and hours using Python arithmetic operators.
Total Seconds 5000
■ Your Tasks
1. Convert 5000 seconds into total minutes using the / operator.
2. Extract the whole hours using the // (floor division) operator.
3. Extract the remaining minutes using the % (modulo) operator.
4. Display all three results.
Hint: Use operators / // % — no conditions or loops needed."""
total_seconds=5000
total_min = total_seconds/60
total_hours = total_seconds//3600
remaining_min = total_min -(total_hours*60)
print(f"Total minutes : {total_min}")
print(f"total hours : {total_hours}")
print(f"Remaining Time : {remaining_min}")

"""■ Task B: Area of Room
Scenario
■ Given Data
Calculate the area and perimeter of a rectangular room using standard geometry formulas.
Length 12.5 ft
Width 10 ft
■ Your Tasks
1. Calculate the Area (Length × Width).
2. Calculate the Perimeter ( 2 × (Length + Width) ).
3. Display both results with appropriate units."""
length=float(input("Enter length :"))
width =float(input("Enter width :"))
Area = length*width
perimeter =2*(length+width)

print(f"Area :{round(Area,2)}")
print(f"Perimeter :{round(perimeter,2)}")

"""■ Task C: Mobile Bill Calculator
Scenario
■ Given Data
A telecom company charges its users separately for call duration and SMS messages. Calculate the monthly bill.
Call Duration 120 minutes @ Rs 2.5 / min
SMS Messages 30 messages @ Rs 1.0 / SMS
■ Your Tasks
1. Calculate call charges (minutes × rate per minute).
2. Calculate SMS charges (messages × rate per SMS).
3. Calculate total bill (call charges + SMS charges)."""
call_duration=120
prize_per_minutes=2.5
sms_message=30
prize_per_sms=1

call_charges = call_duration*prize_per_minutes
sms_charge = sms_message*prize_per_sms
total_bill = call_charges+sms_charge

print(f"call change :{call_charges}")
print(f"sms charge : {sms_charge}")
print(f"Total bill :{total_bill}")

"""■ Task D: String Manipulation & Tuple Conversion
Scenario
■ Given Data
Work with Python string methods and tuple conversion to transform raw text into a structured data type.
value = "python is high level programming language"
■ Your Tasks
1. Capitalize the first letter of each word in the string.
2. Split the resulting string into individual words.
3. Convert the list of words into a tuple.
4. Display the final tuple."""

value = "python is high level programming language"
b = value.split()
c = b[0].capitalize(),b[1].capitalize(),b[2].capitalize(),b[3].capitalize(),b[4].capitalize(),b[5].capitalize()
print(c)

#or

value = "python is high level programming language"
for_capitalized = value.title()
words = for_capitalized.split()
final_tuple = tuple(words)
print(final_tuple)



