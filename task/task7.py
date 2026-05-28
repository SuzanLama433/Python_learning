"""01 Print All Even Numbers Between 1 and 50
Write a Python program using a loop to print all even numbers between 1 and 50 (inclusive) on a single line.
Requirements:
◆ Use a for loop with range()
◆ Use the modulus operator (%) to check for even numbers
◆ Print all results on one line separated by spaces"""

for i in range(1,51,1):
    if i%2==0 :
        print(f"{i}",end=" ")

"""02 Sum of All Numbers in a List
Write a Python program that uses a loop to compute and display the sum of all elements in the given list.
Requirements:
◆ Use a for loop to iterate through the list
◆ Accumulate the total in a variable (do NOT use sum())
◆ Print the result in the exact format shown below """

input = [10, 20, 30, 40, 50]
a =0
for i in input:
    a = a+i
print(a)

"""3 Multiplication Table of a User-Entered Number
Write a Python program that asks the user to enter a number and prints its complete multiplication table from
1 to 10.
Requirements:
◆ Use input() to accept the number from the user
◆ Use a for loop running from 1 to 10
◆ Format each line as: num x i = result"""

user = int(input("Enter your mul num :"))

for i in range(1,11):
    print(f"{user} * {i} = {user*i}")

"""04 Count Vowels in a Given String
Write a Python program that accepts a string from the user and counts the total number of vowels (a, e, i, o,
u) it contains, ignoring case.
Requirements:
◆ Use a for loop to iterate over each character
◆ Check both uppercase and lowercase vowels
◆ Print the final vowel count"""

user_input = input("Enter your words :")
vowel_count = 0

for i in user_input:
    if i.lower() in "aeiou":
        vowel_count +=1
print(f"your vowel count is :{vowel_count}")

"""05 Filter Names Starting with 'S' (Case-Insensitive)
Write a Python program that filters names beginning with the letter 'S' or 's' from the given list and stores
them (all lowercase) in a new list.
Requirements:
◆ Iterate over the input list using a for loop
◆ Use .lower() for case-insensitive comparison
◆ Store all matching names in lowercase in a new list"""

names = ["sujan","anjan","anju","hari","samir","amar"]

for i in names:
    if i.lower().startswith("s"):
        print(i)

"""06 Count Uppercase and Lowercase Characters
Write a Python program that loops through the sample string and counts the number of uppercase and
lowercase letters separately. Spaces and punctuation must be ignored.
Requirements:
◆ Use a for loop to examine each character
◆ Use .isupper() and .islower() built-in methods
◆ Print both counts in the exact format shown below """
user_input = input("Enter your words :")
lower = 0
upper = 0

for i in user_input:
    if i.isupper():
        upper +=1
    elif i.islower():
        lower +=1
print(f"lower count :{lower}")
print(f"upper count :{upper}")

"""07 Character Frequency Dictionary
Write a Python program that takes a string and builds a dictionary where keys are unique characters and
values are the number of times each character appears.
Requirements:
◆ Use a for loop to iterate through the string
◆ Store character counts in a dictionary
◆ Do NOT use Counter from the collections module"""
user_input = input("Enter your words :")
user_dis = {} 

for i in user_input: #programming
    if i not in user_dis:
        user_dis[i]=1
    else:
        user_dis[i] += 1
print(user_dis)
        
student = {
    'name':'sujan'
}

student['game']=1
print(student)
"""08 List of Squares from 1 to 10
Write a Python program that uses a for loop to build a list containing the squares of all integers from 1 to 10,
then prints the list.
Requirements:
◆ Use a for loop — do NOT use list comprehension
◆ Use the ** operator to compute each square
◆ Print the final list"""
squre = [1,2,3,4,5,6,7,8,9,10]

for i in squre:
    print(i**2,end=" ")

"""09 Fibonacci Series up to 10 Terms
Write a Python program that generates and prints the first 10 terms of the Fibonacci series using a loop.
Requirements:
◆ Use a for loop for exactly 10 iterations
◆ Each term is the sum of the two preceding terms
◆ Print all terms on a single line separated by spaces """
a = 0
b = 1

for i in range(10):
    print(a,end=" ")
    a,b = b,a+b
    
"""10 Password Validity Checker
Write a Python program that validates a user's password against the five rules below. Clearly indicate which
specific requirements were NOT met.
Requirements:
◆ At least 8 characters long
◆ Contains at least one uppercase letter (A-Z)
◆ Contains at least one lowercase letter (a-z)
◆ Contains at least one digit (0-9)
◆ Contains at least one special character (! @ # $ % ^ & * etc.)"""

user_name = input("Enter your username: ").lower()
user_pass = input("Enter your Password: ")

special_chars = "!@#$%^&*?"

upper = False
lower = False
digit = False
special = False

for i in user_pass:

    if i.isupper():
        upper = True

    if i.islower():
        lower = True

    if i.isdigit():
        digit = True

    if i in special_chars:
        special = True


if len(user_pass) >= 8 and upper and lower and digit and special:
    print("Your password is strong.....")

else:
    print("Password is INVALID. Requirements not met:")

    if len(user_pass) < 8:
        print("[x] Must be at least 8 characters long")

    if not upper:
        print("[x] Must contain at least one uppercase letter")

    if not lower:
        print("[x] Must contain at least one lowercase letter")

    if not digit:
        print("[x] Must contain at least one digit")

    if not special:
        print("[x] Must contain at least one special character")
    
"""11 Find Palindromes in a Mixed List
Write a Python program that loops through a list containing both strings and integers and collects only the
elements that are palindromes (read the same forwards and backwards).
Requirements:
◆ Iterate over the input list using a for loop
◆ Convert integers to strings before comparison
◆ Use slicing [::-1] to reverse and check"""

input_user = ['apple', 'racecar', 'carac', 'mam', 'orange', 121, 331]
palimdrom =[]

for i in input_user:
    value = str(i)
    if value == value[::-1]:
        palimdrom.append(i)
print(f"Palimdroms :{palimdrom}")


    
    