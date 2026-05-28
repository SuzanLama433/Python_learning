"""Sets : collection of item(data structure) which is mutable , unorder and not support duplication 
set represent by {}"""
# a = {"sujan",13,2,"hari",333,40,"sujan"}

# a.add("manoj")

# a.update({55,66})

# print(a)
# a.clear()
# a.remove("sujan")
# a.discard("sujan")
# a = {1,2,3,4,5}
# b ={2,4,6,8}
# c= a.intersection(b)
# c = a.union(b)
# c = b.difference(a)
# c = b.symmetric_difference(b)
# a.intersection_update(b)
#frozenset
# v= frozenset({1,2,3,4,5})
# v.intersection_update(b) --->cannot update 
# print(v)
# print(type(v))
# old_emp = {"himal","sajan","suman","pramod"}
# new_emp ={"himal","saroj","sujan","saurab"}

# result_old_emp = old_emp.intersection(new_emp)
# result_new_emp = new_emp.difference(old_emp)
# print(f"old employee :{result_old_emp}")
# print(f"new employee :{result_new_emp}")

# post1 = {"#ai","#python","#ml"}
# post2 = {"#django","#python","#ai"}
# post3 = {"#mern","#ai","#learn","#js"}

# c = post1.intersection(post2,post3)
# b = post1.difference(post2).difference(post3)

# print(c)
# print(b)

# a = {2,1,3,4,6}
# print(a)

# Input = [1, 2, [3, 4], 5, [6, 7], 8]
# #Output : [3, 4, 6, 7]

# c = Input[2]
# d = Input[4]
# print(c+d)

# Input = [1, 2, 3, 4, 5, 6]
# Output = [6, 2, 3, 4, 5, 1]
# Input , Output = Output , Input
# print(Input)

# Input[0] , Input[-1] = Input[-1], Input[0]
# print(Input)
# Input = ['a', 'b', 'c', 'd']
# b = " ".join(Input)
# c = b.upper()
# d = c.split()
# print(d)
