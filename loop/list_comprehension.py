# list comprehension--> it is error free and used to clean the code in one line 
# creating new list from existing list
# syntax :[expression for item in iterable]

# avoid when nested loop ,multiple condition

a=["sujan","sujal","ram","hariii"]

# b=[5,5,3,6]
'''b=[]
for i in a:
    b.append(len(i))
    
print(b)'''

# b=[len(i) for i in a]
# print(b)

# a=[1,2,3,4,5]
# b=[5,4,3,2,1]

# c=[]
# for i in range(5):
#     c.append(a[i]+b[i])
    
# print(c)

# c=[a[i]+b[i] for i in range(5)]
# print(c)


# if statment inside loop
# syntax :[expression for i in iterable if condition]
a=[1,2,3,4,5,6,7]
b=[]

# for i in a:
#     if i%2 == 0:
#         b.append(i)
        
# print(b)

# b=[i for i in a if i%2!=0]
# print(b)

# if else inside loop
# syntax : [true_expression if condition else false_expression for item in iterable]
a=[1,2,4,3,5]

# b=["odd","even","even","odd",'odd']

"""b=[]
for i in a:
    if i%2==0:
        b.append("even")
    else:
        b.append("odd")
        
print(b)"""

ans=["even" if i%2==0 else "odd" for i in a]
print(ans)