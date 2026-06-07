#scissor paper rock game
import random
a = "Welcome to Sicssor paper rock game"
print(a.center(70,"."))

print('''
      REMEMBER
      S = sicssor
      P = paper
      R = Rock
      
      Rules
      S beats P
      P beats R
      R beats S
      ''')

user_input = input("""Enter your Choice ["S","P","R"]:""")
user_input = user_input.upper()
computer = random.choice(["R","P","R"])

print(f"Your choic is :{user_input}")
print(f"Computer Choice is :{computer}")

if (user_input == "S" and computer == "P") \
    or (user_input=="p" and computer == "R") \
    or (user_input == "R" and computer=="S"):
        print("You win!!!!!!")
elif user_input == computer:
    print("Draw game!!!!")
elif user_input not in ["S","P","R"]:
    print("Enter valid char ['R','P','S']")
else:
    print("Computer win!!!!!!!")



