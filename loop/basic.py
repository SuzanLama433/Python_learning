# Loop : loop are used repeat instruction
'''
it is programming structure that repeat a block of code until some condition match or number of iteration

Type of loop :
For loop 
while loop


For loop:
loop are use for  predetermine number 
it is used for sequence traversal(list,tuple,set,dict,range)

syntax:
for item in somethings:
    block of code
'''

# color=['red','blue',"orange","green"]

# for i in color: #0,1,2,3
#     print(i) #red
    
# a="sujan"

# for i in a:#0
#     print(i)

# a={
#     "name":"sujan",
#     "age":88
# }

# for i,j in a.items():
#     print(i,j)


# range : range(start,end,step)

# for i in range(10): #0,1,2,3,4---9
#     print("sujan",i)
# n=int(input("Enter your multiplication number : "))
# for i in range(1,11):
#     # print(n,"x",i,"=",n*i)
#     print(f"{n} X {i} = {n*i}")

# if inside loop
# a=[1,2,3,4,5,6]

# for i in a:
#     if i%2!=0:
#         print(i)



# names=["manoj","Suyog","sujan","hari"]
# v=[] #suyog,sujan
# for i in names:
#     if i.lower().startswith("s"):
#         v.append(i)   
# print(v)

# for i in range(20,2,-2):
#     print(i,end=" ")

"""while loop : run untill codition is true
syntax:
while condition:
    block of code

"""
'''
While : run until some codition is true

syntax :

while condition:
    block of code
'''

# a=20
# while a>2:
#     print("hello world")

# while True:
#     print("okey !!!")

# hello world
# hello world
# hello world
# hello world


# a=5 #initial point

# while a>0: #stod condition
#     print("hello world",a)
    
#     # a=a+1
#     a-=1 #step


# guessing game
# secret="sujan"
# guess="" #sujan
# c=0 #5

# while c<5:
#     guess=input("Enter your Guess word : ") #hari
#     if guess==secret:
#         print("correct guess")
#         break
#     c+=1

# else:
#     print("your limit is over")

'''
for loop
- no. of iteration is known(known number)
- less chance of infinite loop
- range
- perfomance is faster as compare while 

while loop
- unknown number of iteration
- high chance of infinite
'''

# import time

# start1=time.time()
# for i in range(100000000):
#     pass
# end1=time.time()

# print("for loop",end1-start1)

# start2=time.time()
# a=0
# while a<100000000:
#     a+=1
# end2=time.time()

# print("while loop",end2-start2)



# nested loop 

# a=["sujan","hari","ram"]
# for i in a:
#     print(i)
#     for j in i:
#         print(j)



#task
# i = 1
# user_input = int(input("Enter yoo want mul num :"))

# while i<=10:
#     mul = user_input*i
#     print(f"{user_input} * {i} = {mul}")
#     i +=1

# output = "my name is sujan"
# index = 0

# # Loop until the index reaches the length of the string
# while index < len(output):
#     # Print the character at the current index
#     # end="" keeps the characters on the same line if you want the "Expected Output" look
#     print(output[index])
    
#     # Increment the index to move to the next character
#     index += 1

# # Print a newline at the end
# print()