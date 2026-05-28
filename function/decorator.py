'''
                    ==============Decorator==============
it is a decorator that takes another function as argument and add some feature and
return in new function
@ represent the decorator

'''
def outer(func): #func==show
    print("this is inner function....")
    def inner():
        print("this is innner function")
        func() #show()
    return inner
@outer
def show():
    print("this is another argument")
show()