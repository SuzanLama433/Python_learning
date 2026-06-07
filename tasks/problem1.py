"""1️⃣ Type Conversion Convert the string '100.5' into an integer without losing accuracy in steps, then print
the value and its type."""
# num = "100.5"
# num =float(num)
# num =int(num)
# print(num)
# print(type(num))

"""2️⃣ User Input & Age Calculation Ask the user for their birth year and calculate their age in 2025. Use explicit
type conversion where needed."""

# user_input = int(input("Enter your dob year :"))
# age_cal = 2025-user_input
# print(f"your age is {age_cal}")

"""3️⃣ Variable Swapping Challenge Swap two variables using only assignment operators without using a third
variable:"""
# a = 15
# b = 25
# a,b =b,a
# print(a,b)
a = 15
b = 25
a = a +b
b = a-b
a=a-b
print(a,b)

"""4️⃣ Identity vs Equality (Integers & Lists) Predict the output:
x = 256
y = 256
print(x is y)
a = [1,2,3]
b = [1,2,3]
print(a is b)"""
#ans
"""1.true
2.false"""

"""Boolean Expression (Operator Precedence) Evaluate the following and explain the order of operations:
a = 10
b = 20
c = 5
print(a > b or b > c and not a < c)"""
#ans :true

"""6️⃣ Chained Comparisons Predict the output:
a = 10
b = 5
c = 10
print(a > b == c) 
print(a != b >= c)"""
#ans:false,false

"""7️⃣ Arithmetic with Precedence Predict the result of:
a = 3
b = 5
c = 7
d = 2
print(a + b * c // d - b % a)"""

#ans:18

"""8️⃣ Identity & Equality (Large Integers) Predict the output:
a = 1000
b = 1000
print(a is b)
print(a == b)"""
#ans: true ,true

"""9️⃣ Identity & Equality (Floats) Predict the output:
x = 10.0
y = 10.0
print(x is y)
print(x == y)"""
#ans true ,true

"""🔟Tuples & Strings Identity Predict the output:
t1 = (1,2,3)
t2 = (1,2,3)
print(t1 is t2)
s1 = "hello"
s2 = "hello"
print(s1 is s2)""" 
#ans true ,true

"""1️⃣1️⃣ Boolean Logic with and, or, not Predict the output:
a = 5
b = 10
c = 15
print(a < b and not b > c or c == 15)"""
#ans : true

"""1️⃣2️⃣ Combined Arithmetic Challenge Evaluate the following expression step by step:
a = 3
b = 5
c = 7
d = 2
print(a + b * c // d - b % a)"""

#Ans:18
