'''Define a global variable name = "Alice".
Write a function change_name() that:
Declares a local variable name = "Bob" (without global).
Then uses global name to change the global name to "Charlie".
Print name before and after calling the function'''

name = "Alice"
def change_name():
    local_name ="bob"
    print(f'local name:{local_name}')
    global name
    name = "sujan"
    return name
    
print(name)
print(f'change global name :{change_name()}')
    
change_name()

#Create a lambda function calculate that takes three arguments (a, b, c) and returns (a + b) * c.

a = lambda a,b,c:(a+b)*c

print(a(2,3,4))

#Create a lambda function reverse_string that takes a string and returns it reversed (e.g., "hello" → "olleh")

reverse_string = lambda a : a[::-1]
print(reverse_string("hello"))

#Create a lambda function square that takes a number and returns its square.

squre = lambda number : number**2

print(squre(2))

'''Task 2: Default Arguments
Create a function greet_user() that takes name with a default value of "Guest" and greeting with a default value of "Hello". 
The function should print the greeting message. Call this function:
Without any arguments
With only the name argument
With both arguments'''

def greet_user(name="Guest",greeting ="Hello"):
    # print(f'your name is {name}')
    # print(f'you greeting {greeting}')
    print(f'{greeting} , my name is {name}')
    
#without any argu
greet_user()
#with only the name argu
greet_user(name="sujan")
#with both agru
greet_user(name='Sujan',greeting="Laso")

#bank system

balance = 10000

def prabhu_bank():
    global balance

    print("=============== Welcome to Prabhu Bank ===========")

    while True:
        print("""
                Welcome to Prabhu Bank
                Choice:
                1. Deposit money
                2. Withdraw money
                3. Check balance
                4. Exit
              """)

        choice = input("Enter your choice from 1 - 4: ")

        if choice == "1":
            deposit_amt = int(input("Enter deposit money: "))
            balance += deposit_amt
            print(f"Rs {deposit_amt} is credited to your account.")
            print(f"Updated balance is Rs {balance}")

        elif choice == "2":
            withdraw_amount = int(input("Enter withdraw amount: "))

            if withdraw_amount <= balance:
                balance -= withdraw_amount
                print(f"Rs {withdraw_amount} is debited from your account.")
                print(f"Remaining balance is Rs {balance}")

            else:
                print("Insufficient balance")

        elif choice == "3":
            print(f"Your total balance is Rs {balance}")

        elif choice == "4":
            print("Thank you for visiting us...")
            break

        else:
            print("Please enter a number from 1 - 4")


prabhu_bank()
