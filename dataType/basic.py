# data type :classification data which variable hold
'''
primitive data type : basic data type ,inbuilt,single value
Non-primitive data type :formed by primitive data type,multiple value :[12,12,3,45]

======================================================
                    Data type 
-->numeric Data type (int , float,complex)
-->sequence data type(string, list [],tuple(),range ())
-->Sets :unorder (set, frozenset) --> {}
-->map :dictionary
-->Binary Data type 
-->boolean data type
-->None data type 
=======================================================
'''


# numeric Data type : it represent number
# integer : int : it represent all positive number,negative number and also zero 
# float : it represent all decimal
# complex number :combination real number and imaginary number
# a=4.5j
# print(type(a))
# print(a)

"""type conversion:the process of converting one data type to other
two types:
1. types implicit(data convesion): python interpreter automatically convert one data types to other
2.type explicit(type casting): python developrt convert one date type to anothe
"""
# a = 5
# b = 2.3
# c =a+b
# print(c)
# print(type(c))

#int --> float , complex
#float --> int
#str --> int, float,list , tupple ,set
#list ---> str ,tupple,set

# a= "12.33"
# b = float(a)
# b = int(b)
# print(b)

# a = [1,4,3,5,6,8]
# b = str(a) #"[1,4,3,5,6,8]"
# b = tuple(a)
# b = set(a)
# print(b)
# print(type(b))

# a = {
#     "name":"sujan",
#     "age":88
# }

# b = list(a.items())
# print(b)
# print(type(b))

# a = [1,2,2,3,3,4,5,6] #remove duplication
# b = set(a)
# c = list(b)
# print(c)

# a = "Python is easy and python is english structure" 
# b = a.lower().split()
# c = set(b)
# print(c)




