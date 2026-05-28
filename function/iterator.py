'''iterator : object that contain countable number value (collection of items)
'''
#high order function : map , filter ,reduce

# a=["sujan","hi","gdfghjk"]

# print(max(a,key=len))

#map: it applies special function in each item of iterator
#syntax: map(function_name,iterator)

# n =[2,3,4,5,33]
# def show(n):
#     return n*n
# ans = map(show,n)
# print(list(ans))

# using lambda
# print(list(map(lambda n:n*n,n)))

# task
# radius = [9,18,2,5,50]
# circle =[]
# def circle_area(radius):
#     return 3.1415*radius**2

# ans = map(circle_area,radius)
# circle.append(list(ans))
# print(circle)

# using lambda

# print(list(map( lambda radius:3.1415*radius**2,radius)))

# a =["sujan", "ram","hari"]
# op =[]

# def show(a):
#     return a.upper()

# ans = map(show,a)
# op.append(list(ans))
# print(op)

# using lambda

# print(list(map(lambda a :a.upper(),a)))

# fitler: it filter based function return true or false
#syntax: filter(function,iterator)
# a=[1,2,3,4]

# def show(a):
#     return a%2==0

# v = filter(show,a)
# print(list(v))

# # using lambda

# print(list(filter(lambda a:a%2!=0 , a)))

# a=[1,2,3,4,5,6,7,8,9,10]

# def show(a):
#     return a%3==0

# v = filter(show,a)
# print(list(v))

# using lambda
# print(list(filter(lambda a : a%3==0,a)))

#reduce: 
# from functools import reduce
# a=[1,2,3,4,5,6]
# def show(x,y):
#     return x+y

# v =reduce(show,a)
# print(v)

