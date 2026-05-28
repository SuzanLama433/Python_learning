'''
string: sequene of char that is enclosed with single quote , doble,  triple 
len -->length
'''
#a= 'he said,"i want ti learn python"'
#a = "what's"
#a= """ my name is sujan 
# and 
# i am form bajrabarahi"""

# a = 'hi'
# b = len(a)
# print(b)

#index : the way of accessing element by their position
# a = "my name is sujan"
# print(a[::-1]) #count from opposite 
# print(a[2])

#slicing : the way of accessing part of element 
#syntax : variable_name[start:end:step]

# a = "my name is sujan"
# print(a[3:7:1])
# print(a[3:7:2])
# print(a[6:2:-1]) #eman
# print(a[3:1])
# print(a[:4])
# print(a[::])
# print(a[::-1])
# print(a[3:10:1])

# web = "sipalaya Info Tech"
# print(web[13:8:-1])
# print(web[-5:8:-1])
# print(web[13::-1])

# a = "2"
# b = "34"
# print(a+b)
'''
========================================================
                 method
========================================================
'''
# a = "my Name is Sujan lama" 
# b = "Welcome"
# print(a.upper())
# print(a.lower())
# print(a.title())
# print(a.swapcase())
# print(a.casefold()) #strickly change to lower
# print(a.capitalize())
# print(b.center(20,"*"))
# print(a.replace("Name","name")) #case sensitive
# print(a.index("m"))
# print(a.rindex("m"))
# print(a.count("a"))

# py = """python is a high-level, general-purpose programming language known for 
# its simplicity and readability. It supports multiple paradigms, including 
# object-oriented, procedural, and functional programming.
# """
# user = input("enter you want count :")
# print(py.count(user))

# a = input("Enter you sentence :")
# print(a.replace(" " ,"_"))

# a = "mynamesujan"
# # print(a.isalnum())
# # print(a.isalpha())
# # print(a.isascii())
# print(a.isdigit())

#strip and split 
# a = " !!!!!  sujan!!!!"
# b = "www.ram.com"
# # print(a.strip(""))
# print(b.removeprefix("www.").removesuffix(".com")) 
# print(a.lstrip(".com"))
# print(b.rstrip("@gmail.com"))

#split
# a = "sujan12@gmail.com"
# b = "my name is sujan lama"
# print(a.split())
# print(b.split())

# print(a.rindex("j"))