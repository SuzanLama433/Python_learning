'''variable : container which it is used to store value

types of variable
local variable:those variable which is declare inside the function
global variable: those variable which is declare outside the function
course ="django" #global varibale

def show():
    course="data science" #local variable
    print(course)
show()
'''

# a=12 
# def show():
#     x =22
#     print(x)
#     print(a)
    
# show()

# print(a)
# print(x) #-->cannot calling x from func
#local variable cannot print at outside the function
#global value can calling inside the function but cannot change value but use global keyword for change global valu


# a=22
# def show():
#     global a
#     a=a+3
#     print(a)

# show()


#task
# a=[1,11,22,33]
# s=0

# def sum():
#     global s
#     for i in a:
#         s+=i
#     print(s)
    
# sum()