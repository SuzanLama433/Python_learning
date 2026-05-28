"""Exception handling: the process handling unexcepted event when program is run
try:
    block of code
except:
    error_message

type error
1.compile time error : SyntaxError, IndentationError
2.Run time error : TypeError , IndexError, ZeroDivisionError
3.Logical Error
"""

# try:
#     def show():
#         print("hello sipalaya")
#         print("2"+2)
#     show()
# except:
#     print("some error occor")
# print("some important code is here")

# try:
#     def show(a,b):
#         if b<0:
#             raise ValueError(f'b cannot be zero')
#         print("hello sipalaya")
#         print("2"+2)
#         print(a+b)
#     show(2,3)
    
# except Exception as e:
#     print(e)
# except TypeError :
#     print("type error")
# except:
#     print("error occur")
    
# print("some important code is here")

# age = int(input("Enter your age: "))
# name = input("Enter your Name: ")

# try:
#     if age > 0 and len(name) > 3:
#         print(f"Your name is {name} and age is {age}")
#     else:
#         raise ValueError("Invalid input")

# except ValueError as e:
#     print(e)

#finally:

# def show():
#     try:
#         print("my name is sujan lama")
#         return 1
#     except:
#         print("erroorrrrrr")
#     finally:
#         print("this is my important code")
        
# show()