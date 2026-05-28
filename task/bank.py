balance =10000

def deposite():
    global balance
    deposit_amt = int(input("Enter deposit money :Rs "))
    balance += deposit_amt
    print(f"Rs {deposit_amt} is credited to your account.")
    print(f"Updated balance is Rs {balance}")

def withdraw():
    global balance
    withdraw_amount = int(input("Enter withdraw amount :Rs "))

    if withdraw_amount <= balance:
        balance -= withdraw_amount
        print(f"Rs {withdraw_amount} is debited from your account.")
        print(f"Remaining balance is Rs {balance}")

    else:
        print("Insufficient balance")

def total_balance():
        print(f"Your total balance is Rs {balance}")


def prabhu_bank():
    print("===========welcome to prabhu bank============")
    print("""
                Choice:
                1. Deposit money
                2. Withdraw money
                3. Check balance
                4. Exit""")
    while True:
        choice = input("Enter your choice from 1 - 4 :")
        if choice=="1":
            deposite()
        elif choice =="2":
            withdraw()
        elif choice =="3":
            total_balance()
        elif choice=="4":
             print("Thank you for visiting us...")
             break
        else:
            print("Please enter a number from 1 - 4")
            
                
prabhu_bank()