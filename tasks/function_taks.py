'''Function Task
Write a Python function to find the maximum of three numbers.
Write a Python function to sum all the numbers in a list.
Write a function that take list of string and show only string  which are start with s
Write a Python function to multiply all the numbers in a list
Write a Python function to calculate the factorial of a number
Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
Write a Python program to print the even numbers from a given list'''

#Write a Python function to find the maximum of three numbers.

def max_value(a,b,c):
    return max(a,b,c)
    
print(max_value(2,3,4))


def maximum(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
       return b
    else:
      return c

print(maximum(4,5,6))
    
#Write a Python function to sum all the numbers in a list.


def sum_function():
    a =[1,2,3,4,5,7]
    sum_num =sum(a)
    return sum_num

print(sum_function())

def sum_func():
    a = [1,2,3,4,5,7]
    total =0
    for i in a:
        total+=i
    return total
print(sum_func())

#Write a function that take list of string and show only string  which are start with s

def show():
    names =["sujan","anjan","rohan","suman"]
    name_start_with_s =[]
    
    for i in names:
        if i.lower().startswith("s"):
             name_start_with_s.append(i)
    return name_start_with_s
        
print(show())

#Write a Python function to multiply all the numbers in a list

def mul_func():
    num = [2,3,4,5]
    total_mul =1
    for i in num:
        total_mul*=i
        
    return total_mul

print(mul_func())

#Write a Python function to calculate the factorial of a number

def factorial_func(num):
    fact = 1
    for i in range(1,num+1):
        fact*=i
    return fact

print(factorial_func(5))
  
#Write a Python function that takes a number as a parameter and checks whether the number is prime or not.

def prime_num(num):
    if num<=1:
        return 'enter num from 2'
    else:
        for i in range(2,num):
            if num%i==0:
                return "not prime"
            else:
                return "yes prime"
print(prime_num())

num = int(input("Enter a number :"))
if num<=1:
    print("enter num from 2:")
else:
    for i in range(2,num+1):
        if num%i==0:
            print("not prime..")
            break
    else:
        print("Yes prime...")
      
  
#Write a Python program to print the even numbers from a given list.

def even_num(even_list):
   
    even_list1=[]

    for i in even_list:
        if i%2==0:
            even_list1.append(i)
    return even_list1    
        
print(even_num([1,2,3,4,5,6]))