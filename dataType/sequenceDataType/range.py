"""Range :  it is immutable sequence of number which used for loop
syntax: range(start,stop,step)"""
# a = range(2,5)
# print(a)
# print(type(a))

numbers =[2,3,6,8]
for i in range(len(numbers)):
    numbers[i]+=i
print(numbers)