""" Print Numbers 1 to 10 Beginner
Write a program to print numbers from 1 to 10 using a while loop."""
i = 1
while i<=10:
    print(i,end=" ")
    i+=1

"""2 Keep Taking Input Until 'stop' Beginner
Continuously prompt the user for input. Exit the loop only when the user types 'stop'"""

while True:
    user_input = input("Enter something (or 'stop'to quit) :")
    if user_input =="stop":
        break
    print("you entred :",user_input)
print("program end")
    
"""3 Mobile PIN Verification (3 Attempts) Intermediate
Simulate a PIN verification system. The user gets exactly 3 attempts. Show an error message after each wrong
attempt and lock the account when all attempts are exhausted."""    

my_key = 123
count = 3
while count>0:
    your_pin = int(input("enter your pin :"))
    if your_pin==my_key:
        print("your pin is correct!!",your_pin)
        break
    else:
        count -=1
        if count>0:
            print(f"your pin is wrong ,you attempt {count} times")
        else:
            print(f"your attempt {count},lock your pin")
        
#or

a = int(input('enter: '))
while my_key != a and count > 1:
    count -= 1
    print(f'invalid pin!!')
    print(f'attempt left is {count}')
    a = int(input('enter: '))

if my_key==a:
    print("your pin is correct!!!")
else:
    print("lock you pin")
    
"""4 Sum of Digits of a Number Intermediate
Given a number, calculate the sum of all its individual digits.
Expected Output
Enter a number: 1234
Sum of digits: 10 """

user_input = int(input("Enter your num :"))
total = 0
while user_input>0:
    last_dig = user_input%10
    total +=last_dig
    user_input = user_input//10
print(total)
    
"""5 Print All Even Numbers from 2 to 20 Beginner
Print all even numbers from 2 to 20 using a while loop.
Expected Output
2 4 6 8 10 12 14 16 18 20"""
i =1

while i<21:
    if i%2==0:
        print(f"{i}",end=" ")
    i += 1

"""6 Reverse a Number Intermediate
Convert a number into its reverse using a while loop. Do not use string slicing or any built-in reverse method."""

user_input = int(input("Enter num :"))
reverse = 0

while user_input>0:
    last_dig = user_input%10
    reverse = reverse*10 + last_dig
    user_input =user_input//10
print(reverse)

"""7 Count the Digits of a Number Find how many digits are in a given number. Do not convert the number to a string."""
user_input = int(input("Enter num for count :"))
count =0
while user_input>0:
    user_input =user_input//10
    count+=1
print(count)

"""8 Find Smallest and Largest (No Built-in Methods) Given the list below, find the smallest and largest values without using min(), max(), or sort().
a = [8, 3, 5, 12, 5, 8, 9, 19]"""

a = [8, 3, 5, 12, 5, 8, 9, 19]
largest =a[0]
smallest =a[0]

for i in a:
    if i<smallest:
        smallest=i
    if i>largest:
        largest=i
print(smallest)
print(largest)

"""9 Print String Character by Character Using a while loop and an index variable, print each character of the string below one by one.
output = "my name is sujan"""

user_input ="my name is sujan"
index =0
while index<len(user_input):
    print(user_input[index])
    index+=1
print()

"""Display a multiplication table for numbers 1 to 5 (each up to x10) using nested while loops."""

num =1 

while num<=5:
    print(f"mul of table:{num}")
    
    i = 1
    while i<=10:
        print(f"{num} X {i} = {num*i}")
        i +=1 
    print()
    num+=1
    
"""Display All Prime Numbers Within an Interval Advanced
A prime number is a number greater than 1 with no divisors other than 1 and itself. Write a program that finds all
prime numbers between a given start and end."""

start = 10
end = 20
prime_numbers = []
num = start

while num <= end:
    if num > 1:
        is_prime = True

        divisor = 2
        while divisor < num:
            if num % divisor == 0:
                is_prime = False
                break
            divisor += 1

        if is_prime:
            prime_numbers.append(num)

    num += 1

print(f"Prime numbers between {start} and {end}:")
print(prime_numbers)
    
    
    