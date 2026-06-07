"""=============================================DAY 3 TASK============================================="""

"""Task 1: Word Count
Write a Python program that takes a sentence as input from the user, then counts and displays the number of words in the sentence.
"""
#code
user = "my name is sujan"
b = user.split(" ")
print("output",len(b))

"""Task 2: Reverse Word Order
Write a Python program that takes a sentence as input and produces a new string with the words in reverse order, 
while keeping each word in its original form."""
#code
user_input = "hello world! , it's me sujan lama"
b = user_input.split()
c = b[::-1]
rev = " ".join(c)
print(rev)

"""Task 3: Second Largest Number
Write a Python program that takes a list of numbers and prints the second largest number from the list."""
#code
user_input = [2,34,6,82,4,7,9,0,22]
result = sorted(user_input)
print(" 2nd highest num",result[-2])

"""Task 5: Find the Longest Word
Write a Python program that takes a sentence as input from the user, then finds and displays the longest word in the sentence.
"""
#code
a = "Learning Python is really enjoyable"
b = a.split()
c = (max(b, key=len))
print(f"Longest word: {c} ({len(c)} characters)")

"""Task 6: Rotate a List (Without Using a Loop)
Given a list, rotate its elements to the left by 2 positions and print the result. You must not use any for or while loop."""
#code
a = [1, 2, 3, 4]
k= int(input("enter"))
result_1=(a[-k:])
result_2=(a[:-k])
print(result_1+result_2)

"""Task 8: Uppercase All Strings in a List
Given a list of single-character strings, produce a new list where each string is converted to uppercase."""
#code
a = ['a', 'b', 'c', 'd']
result = " ".join(a)
final=(result.upper())
print(final.split())
b = a[0].upper(),a[1].upper(),a[2].upper()

"""Task 9: Simple To-Do List (List Practice)
Practice list operations by building a basic To-Do List system using only Python list methods.
Instructions:
• Create an empty list called tasks.
• Add at least 3 tasks using .append().
• Display all tasks.
• Remove one task using .pop() and print the removed task.
• Mark the first task as completed by adding the text " [DONE]" to it.
• Display the updated task list.
• Clear all tasks using .clear() and print the empty list."""
#code
tasks = []
tasks.append("sleep")
tasks.append("running")
tasks.append("game")

print(f"all task :{tasks}")
b = tasks.pop()
print(f"Remove :{b}")
tasks[0] = tasks[0]+"[DONE]"
print(tasks)
tasks.clear()
print(tasks)

"""Task 10: Marks Calculator
Given a list of marks, calculate and display the following:
Instructions:
• Total sum of marks
• Number of marks
• Average percentage
Constraints:
• No loops (for / while)
• No conditionals (if / else)
• No function definitions (def)
• Use built-in functions only"""
#code
marks = [85, 92, 78, 90, 88]
total = sum(marks)
count = len(marks)
average = total/count

print(f"total: {total} count : {count} averge: {average}%")