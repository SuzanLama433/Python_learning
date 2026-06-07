# #practice task  By sujan lama
# #remove all vowels from string 
# """ Q.N1 Write a Python program that takes a string from the user and removes all vowel 
#  letters (a, e, i,o, u) from it. The program should handle both uppercase and lowercase vowels. """
#  #code
user = input("Enter sentence ")
print(user.replace("a","").replace("e","").replace("i","").replace("o","").replace("o",""))

# """
# Task 2: Palindrome Check (Case & Space Insensitive)
# Write a program that checks whether a given string is a palindrome. 
# The check must ignore spaces and letter case, so phrases with mixed case still work correctly.
# """
# #code
Palindrome = input("Enter palindrome sens")
clean = Palindrome.lower().replace(" ","")
print(clean == clean[::-1])

# """Task 3: Word Frequency Counter
# Write a Python program that contains a predefined paragraph string. Take a word as user
# input and count how many times that word appears in the paragraph (case-insensitive).Display the count.
#     """
# #code
user_sentence = """Write a Python program that contains a predefined paragraph string. Take a word as user
input and count how many times that word appears in the paragraph (case-insensitive).Display the count
# """
a = input("enter ")
print("word",a,"appear",user_sentence.lower().count(a),"times")

# """Task 4: Count Vowels in a Sentence
# Write a program that takes a sentence as input and counts the total number of vowels (a, e, i,o, u) 
# it contains. The count must be case-insensitive.
#     """
# #code
input1 = input("Enter words")
print(input1.count("a")+input1.count("e")+input1.count("i")+input1.count("o")+input1.count("u"))

# """ Task 5: Remove Parentheses and Their Contents
# Given a string containing parentheses ( ) with dynamic content inside them, write a program
# that removes both the parentheses and the text enclosed within them, regardless of length or
# position.
# """
# #code
user = input("Enter your input")
start= user.index("(")
end = user.index(")")
print(user[ :start]+user[end+1: ] )

# """Task 6: Hide Password Characters
# Write a program that stores a username and a password. The program should display the
# username as it is, but mask the password by replacing every character with an asterisk (*) of
# the same length.
# """
# #code
username = input("Enter your user name")
user_password = input("Enter your user password")
len1 = len(user_password)
print("your user name: ", username,"\n your paassword: ",len1*"*")

# """Task 7: Replace Bad Words
# Write a program that takes a sentence and replaces a specific word with another word. For example, 
# replace the word "bad" with "good" in the given text.
# """
# #code
user = input("Enter your words")
print(user.lower().replace("bad","good"))

# """Task 8: Username Cleaner
# Write a program that takes a raw username and cleans it according to the following rules:
# remove leading and trailing spaces, remove all dot (.) characters, and convert the result to
# lowercase"""
# #code
user_input = input("Enter your username :")
print("username :",user_input.lower().split(".")+user_input.lower().split("!"))

# """Task 9: Email Formatter
# Write a program that takes a username and a domain, and combines them into a properly formatted email address."""
# #code
name = input("Enter your name :")
domain = input("Enter your domain :")
result = name+"@"+domain
print(result.lower().replace(" ",""))

# """Task 10: Password Strength Check (Basic)
# Write a program that takes a password and checks the following properties: whether it isalphanumeric, whether 
# it is entirely lowercase, and whether it is entirely uppercase. Display aclear result for each check."""
# #code
enter_password = input("Enter your password")
print("alphanumeric:" , enter_password.isalnum())
print("lowercase:",enter_password.islower())
print("uppercase :",enter_password.isupper())

# """Task 11: Extract Username from Email
# Write a Python program that takes an email address as input and extracts only the username
# portion (the part before the @ symbol)."""
# #code
user_input = input("enter your email")
print("Email :",user_input.lower())
print("User name :",user_input.lower().rstrip("@gmail.com"))

# """Task 12: Replace Spaces with Underscores
# Write a Python program that takes a sentence as input and replaces every space character with an underscore ( _ )."""
# #code
user_input = input("Enter your words :")
print("output :",user_input.replace(" ","_"))
