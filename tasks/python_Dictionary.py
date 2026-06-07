"""Day-4
Day Name Lookup
"""
"""1. Write a Python program that:
• Creates a dictionary mapping numbers 1-7 to day names, where 1 = Sunday and 7 = Saturday.
• Asks the user to enter a number between 1 and 7.
• Displays the corresponding day name.
• Handles invalid input gracefully (e.g., a number outside 1-7 or non-numeric input)."""
#code
weeks = {
    "1" : "Sunday",
    "2" : "monday",
    "3" : "tuesday",
    "4" : "wednesday",
    "5" : "Thursday",
    "6" : "friday",
    "7" : "Saturday"
}
user_input = input("enter 1 to 7: ")
a = weeks.get(user_input,"a number outside 1-7")
print(f"your day :{a}")

"""2. Create a dictionary that stores a student's grades in at least five subjects. Then:
• Print the full grade dictionary.
• Calculate and display the average grade.
• Identify and display the highest and lowest scoring subjects."""
#code
student_grades = {
    "Mathematics": int(input("Enter math marks :")),
    "Science": int(input("Enter scienc marks :")),
    "History": int(input("Enter history marks :")),
    "Computer Science": int(input("Enter computer science marks :")),
    "Economics": int(input("Enter economics :"))
}
average_grade = sum(student_grades.values())/len(student_grades)
height_scoring = max(student_grades.values())
height_scoring_subject = max(student_grades,key=student_grades.get)
lowest_scoring = min(student_grades.values())
lowest_scoring_subject = min(student_grades, key=student_grades.get)
print(f"All student grades : {student_grades.items()}")
print(f"Average Grade : {average_grade}")
print(f"Height Scoring :{height_scoring_subject} {height_scoring}(marks)")
print(f"lowest Scoring : {lowest_scoring_subject} {lowest_scoring}(marks)")

"""Task 03 Updating a Person Dictionary
person = {'name': 'Sujan', 'age': 23, 'city': 'Kathmandu'}
Perform the following operations in order:
1. Add a new key 'job' with the value 'Developer'.
2. Update 'name' to 'Ram Bahadur' and 'age' to 45.
3. Print the final dictionary."""
#code
person = {'name': 'Sujan',
          'age': 23,
          'city': 'Kathmandu'
          }
person.setdefault("job","Developer")
person['name'] = "Ram Bahadur"
person['age'] = 45
print(person)

"""Task 04 Nested Dictionary — Updating a Value
You are given the nested dictionary below:
my_details = {
'name': 'sujan',
'grade': 0,
'address': 'ktm',
'hobbies': {
'sports': 'running',
'game': 'pubg',
'novel': 'xyz',
'anime': 'one piece',
},
'email': 'sujan@gmail.com'
}
Change the value of 'novel' from 'xyz' to 'Harry Potter', then print the updated dictionary."""
#code
my_details = {
'name': 'sujan',
'grade': 0,
'address': 'ktm',
      'hobbies': {
         'sports': 'running',
        'game': 'pubg',
        'novel': 'xyz',
        'anime': 'one piece',
},
'email': 'sujan@gmail.com'
}
my_details['hobbies']["novel"] = "Harry Potter"
print(my_details)
"""Task 05 English-to-Nepali Dictionary App
Build a simple English-to-Nepali translation program using a Python dictionary. Your program should:
• Contain at least 10 English words and their Nepali translations.
• Ask the user to enter an English word.
• Display the Nepali translation if the word exists in the dictionary.
• Print a friendly "Word not found" message if the word is not in the dictionary.
• Allow the user to keep searching until they choose to quit (use a loop).
Extension challenge: Make the lookup case-insensitive so that 'Hello', 'hello', and 'HELLO' all return the same
result."""
#code
val ={
    "mother":"आमा",
    "father":"बुबा",
    "love":"माया",
    "text":"पाठ",
    "school":"विद्यालय"
}
user_input = input("Enter word you want to translate:").lower()
print(f'{val.get(user_input,"word is not found !!")}')
