"""Write a Python function that takes a list of integers as input and 
returns a new list with the elements sorted in descending order, 
but with all odd numbers appearing before all even numbers"""
# using function 
def show(all_num):
    odd_num =[]
    even_num =[]
    for i in all_num:
        if i%2==0:
          even_num.append(i)
        else:
          odd_num.append(i)
    even_num.sort(reverse=True)
    odd_num.sort(reverse=True)
    c =odd_num+even_num
    return c 
print(show([1,2,3,4,5,6,7]))
a=input("Enter your number") #: 1 2 3 4 
a.split() #["1","2"]
v=map(int,a)

# or 
a = [1,2,3,4,5,6,7]
def even(a):
    return a%2==0
v=filter(even,a)
even_rev=list(v)
even_rev.sort(reverse=True)  


def odd(a):
    return a%2!=0

f=filter(odd,a)
odd_rev=list(f)
odd_rev.sort(reverse=True)

b = odd_rev+even_rev
print(b)

# or using lamda
b = [1,2,3,4,5,6,7]
even_rev = sorted(filter(lambda x : x%2==0,b),reverse=True)
odd_rev = sorted(filter(lambda x : x%2!=0,b),reverse=True)
c = odd_rev+even_rev
print(c)




# Extract Lengths of Strings
# Use map() to get the lengths of strings in a list.
# words = ["apple", "banana", "cherry", "date"]
# Output: [5, 6, 6, 4]

words = ["apple", "banana", "cherry", "date"]

def cout(a):
    return len(a)
v = map(cout,words)
print(list(v))

# or 

print(list(map(lambda x : len(x),words)))

"""Filter Palindromic Words
Use filter() to extract words that are palindromes (same forwards and backwards).
words = ["madam", "racecar", "python", "level", "hello"]"""

words = ["madam", "racecar", "python", "level", "hello"]

def palindromes(a):
    return a==a[::-1]
v = filter(palindromes,words)
print(list(v))
# or 
print(list(filter(lambda x:x==x[::-1],words)))

"""Task 1: Filter Names Starting with 'A'
Use filter() to get names that start with the letter 'A' (case-insensitive).
names = ["Alice", "bob", "Anna", "David", "alex"]"""

names = ["Alice", "bob", "Anna", "David", "alex"]

def letter_a(a):
    return a.upper().startswith("A")
v = filter(letter_a,names)
print(list(v))

# or 

print(list(filter(lambda names:names.startswith("A"),names)))

"""Write a Python function that takes two lists of integers as input and returns a
new list containing only the numbers that are present in both lists, but with each number 
appearing only once in the final list."""

a=[1,2,3,4,4,5]
b=[4,5,5,6,7,8]
def no_duplication(a,b):
    a1=set(a)
    a2=set(b)
    final= a1.intersection(a2)
    return final
print(no_duplication(a,b))

# or
print(list(set(filter(lambda x:x in a,b))))


'''Write a Python program that takes two sets as input and returns 
a new set containing the elements that are in the first set but not in the second set,
and the elements that are in the second set but not in the first set.'''

set1={1,2,3,4}
set2 ={3,4,5,6}

print(set(filter(lambda x :x not in set2,set1))|\
    set(filter(lambda x : x not in set1,set2)))

'''Write a Python program to extract only the domain names from a list of URLs and store them in a new list
input=['www.google.com', 'www.youtube.com', 'github.com', 'www.facebook.com', 'openai.com']
output=["google","youtube","github","facebook","openai"]'''

input=['www.google.com', 'www.youtube.com', 'github.com', 'www.facebook.com', 'openai.com']

def show(a):
    return a.replace('www.','').split('.')[0]
print(list(map(show,input)))

# or

print(list(map(lambda x : x.replace('www.','').split('.')[0],input)))

    
    

