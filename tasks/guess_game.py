#guess game
import random
num = random.randint(1,20)
guess =0
print("==========WELCOME GUESS NUMBER=================")

while num!=guess:
    guess = int(input("Enter your guess num : "))
    if guess>num:
        print("guess less num")
    elif guess<num:
        print("guess greater num ")
else:
    print("correct guess!!!")