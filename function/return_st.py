'''return statement : it is used inside the function send value to the caller
point to know:
1.send value back the caller
2.end the function execution 
3.return statement give none when expression is null 
4.it can return multiple value 
'''
# def show(a,b):
#     return a+b,a-b

# sum , sub = show(4,2)
# print(sum , sub)

def avg(a,b):
    return (a+b)/2
print(f"the avg of the given number is {avg(int(input("enter input a:")),int(input("Enter input b:")))} ")