"""1. Reverse a Number
Write a program to reverse an integer."""

num = int(input("Enter a number : "))

reverse=0
while num>0:
    digit = num%10
    reverse =reverse*10+digit
    num = num//10
print(f"Reverse num : {reverse}")