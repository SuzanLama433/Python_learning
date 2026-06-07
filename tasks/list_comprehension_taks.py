#1 Section A: Basic List Operations
"""Generate a list of squares of numbers from 1 to 10.
Expected output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]"""
b=[i**2 for i in range(11)]
print(b)

"""Convert all names in the list ["ram", "hari", "sita", "gita"] to uppercase.
Expected output: ['RAM', 'HARI', 'SITA', 'GITA']"""
names =  ["ram", "hari", "sita", "gita"]
update_name = [i.upper() for i in names]
print(update_name)

"""Find the length of each word in ["apple", "cat", "elephant", "dog"].
Expected output: [5, 3, 8, 3]"""
pet_names = ["apple", "cat", "elephant", "dog"]
update_pet =[ len(i) for i in pet_names]
print(update_pet)

"""Extract the first character of every word from ["python", "django", "flask", "fastapi"].
Expected output: ['p', 'd', 'f', 'f']"""

course = ["python", "django", "flask", "fastapi"]
course_update = [ i[0] for i in course]
print(course_update)

#2 Section B: Filtering Data
"""Q05
From ["Ram", "Sujan", "Hari", "Bibek", "Sita", "Anisha"], keep only names longer than 4 characters.
Hint: Apply a condition after the iteration clause"""
names = ["Ram", "Sujan", "Hari", "Bibek", "Sita", "Anisha"]
update_names = [i for i in names if len(i)>4]
print(update_names)

"""6
Remove all negative numbers from [-5, 3, -1, 8, -9, 0, 4, -2, 7].
Expected output: [3, 8, 0, 4, 7]"""

num = [-5, 3, -1, 8, -9, 0, 4, -2, 7]
update_num = [i for i in num if i>=0]
print(update_num)

"""Create a list of all numbers from 1 to 100 that are divisible by both 3 and 5.
Hint: Use the % operator with two conditions joined by and."""
        
divisible_num = [ i for i in range(100) if i%3==0 and i%5==0 ]
print(divisible_num[1: ])

# for a in range(100):
#     if a%3==0 and a%5==0:
#         print(a)
#3 Section C: Type Conversion & Transformation

"""Convert the list of numeric strings ["1", "2", "3", "4", "5"] into integers.
Expected output: [1, 2, 3, 4, 5]"""

str_num = ["1", "2", "3", "4", "5"]
update_num = [int(i) for i in str_num]
print(update_num)

"""Given prices [1200, 400, 6000, 850, 3500] (NPR, excl. VAT), generate a list of VAT amounts at 13%.
Hint: Multiply each price by 0.13."""
amt = [1200, 400, 6000, 850, 3500]
vat = 0.13
update_amt = [i*vat for i in amt]
print(update_amt)

#4 Section D: Advanced Challenges
"""Q10
Add corresponding elements from two lists: a = [1, 2, 3, 4] and b = [10, 20, 30, 40].
Expected: [11, 22, 33, 44] — Hint: use zip()."""
a = [1, 2, 3, 4]
b = [10, 20, 30, 40]
c = [x+y for x,y in zip(a,b)]
print(c)

"""Flatten the nested list [[1, 2], [3, 4], [5, 6], [7, 8]] into a single flat list.
Expected: [1, 2, 3, 4, 5, 6, 7, 8] — Hint: nested list comprehension."""

a =[[1, 2], [3, 4], [5, 6], [7, 8]]
# # for i in a:
# #     for j in i:
# #         print(j)
      
b=[j for i in a for j in i]
print(b)
"""From the string "education", extract all vowels in the order they appear.
Expected output: ['e', 'u', 'a', 'i', 'o']"""

a = "education"
vowel_word = [ i for i in a if i in "aeiou" ]
print(vowel_word)
# for i in a:
#     if i.lower() in "aeiou":
#         print(i)

"""Given marks [50, 45, 90, 60, 32, 78, 29, 55], create a list showing '<mark>=Pass' (if mark >= 45) or
'<mark>=Fail' otherwise.
Hint: Use a ternary expression (value_if_true if condition else value_if_false)."""

marks = [50, 45, 90, 60, 32, 78, 29, 55]
update_marks =["pass" if i>=45 else "fail"  for i in marks] 
print(update_marks)
