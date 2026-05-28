"""loop control statement : it is used to change flow execution , stop the iteration , or skip iteration

#types
pass
break
continue
else

pass: it is null statement that is used for future code
break:it is used terminate the loop when encounter
continue: it is used sto[ the current iteration but continue next iteration 
"""
# for i in range(10):
#     pass
# print("hello")

# a = [12,13,45,34,64,55]
# for i in a:
#     print(i)
#     if i ==20:
#         break

# for i in range(1,11):
#     if i%2==0:
#         continue
#     print(i,end=" ")

# a = ["sujan","ram","sujal","manoj"]

# for i in a:
#     if i.startswith("s"):
#         continue
#     print(i,end=" ")

# a = [1,2,4,5,0,67]
# for i in a:
#     if i==0:
#         print("0 is found !!")
#         break
# else:
#     print("not found!!")
num = 1

while num <= 5:
    print(f"Multiplication Table of {num}")

    i = 1
    while i <= 10:
        print(f"{num} x {i} = {num * i}")
        i += 1

    print()  # blank line between tables
    num += 1