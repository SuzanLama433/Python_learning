'''argument: a value pass to function when it is called
it's types:
1.positional argument
2.keyword argument
3.default argu
4.arbitrary argu
'''
#positional argument
# def show(name ,age):
#     print(name, age)
# show("sujan",99)
# show(99,"sujan")

#keyword argument
# def show(name , age):
#     print(name,age)
# show(name="sujna",age=88)

#default argument
# def show(name, age, school="moliss"):
#     print(name,age,school)

# show("sujan",98)
# show("anjan",22,"united")

#arbitrary argument
#types:
#1.position arbitrary argument
#2.keyword arbitrary argument

#1.position arbitrary argument: it is start with *
# def show(*a):
#     print(a)
# show(1,2,3,4)

#2.keyword arbitrary argument

# def show(**a):
#     print(a)

# show(name="sujan",age=33,collage="nedfield")

#def show(*args, **kwargs)

# def show(*a,**b):
#     print(a)
#     print(b)
# show(1,2,3,4,5,name="sujan",age=44,collage="nesfield")

#task
# def salary(**a):
#     total =0
#     for i in a.values():
#         total+=i
#     print(f"total : {total}")
# salary(basic=100,food=500,travel=5000,overtime=200)

# def salary(**a):
#     b=a.values()
#     print(sum(b))
# salary(basic=100,food=500,travel=5000,overtime=200)