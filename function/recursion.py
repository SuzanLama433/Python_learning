'''recursion: a function calling itself again and again to complete a value'''

# def show(n):
#     if n==5:
#         return
#     print("hi sujan lama",n)
#     show(n+1)
# show(0)
# def fact(n):
#     if n==1 or n==0:
#         return 1
#     return n*fact(n-1)

# print(fact(6))

def add(n):
    if  n==0:
        return 0
    return n%10+add(n//10)

print(add(123))

# import sys
# sys.setrecursionlimit(4000)
# print(sys.getrecursionlimit())

