# ATM Machine
print("🏧 Welcome to ATM Machine 🏧")

balance = 500000
pin_code = 1234
attempt = 3

while attempt > 0:
    user_input = int(input("Enter your PIN: "))
    
    if user_input == pin_code:

        while True:
            print("""
=================== ATM MENU =====================
1. Check Balance
2. Withdraw Balance
3. Deposit Balance
4. Exit
==================================================
""")

            enter_choice = int(input("Enter your choice [1-4]: "))

            if enter_choice == 1:
                print(f"Your balance is Rs {balance:.2f}")
                
                break

            elif enter_choice == 2:
                withdraw_atm = int(input("Enter withdraw amount: "))

                if withdraw_atm <= balance:
                    balance -= withdraw_atm
                    print(f"Rs {withdraw_atm} debited from your account")
                    print(f"Remaining balance: Rs {balance}")
                    break
                else:
                    print("Insufficient balance!")
                    break

            elif enter_choice == 3:
                deposit_amt = int(input("Enter deposit amount: "))
                balance += deposit_amt

                print(f"Rs {deposit_amt} credited to your account")
                print(f"Updated balance: Rs {balance}")
                break

            elif enter_choice == 4:
                print("Thank you for visiting us!")
                break

            else:
                print("Invalid choice! Please enter between 1-4.")
            break
    else:
        attempt -= 1
        print(f"Wrong PIN! Attempts left: {attempt}")

else:
    print("too many attempt ,your card is block!!!")