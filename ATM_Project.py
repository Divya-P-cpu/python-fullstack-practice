# ATM Machine Mini Project
# Python Practice Project Using Nested While Loops

# Objective: Build the logic of a simple ATM application using nested while loops,
# conditional statements, variables, lists, and user input.
#1. Project Requirements
#No. ATM Operation Expected Logic
#1 Deposit Accept an amount greater than 0, add it to the current balance, and record it in deposit history.
#2 Withdraw Accept withdrawal only when amount is greater than 0 and less than or equal to the available balance. Deduct and record it.
#3 Balance Inquiry Display the current available balance.
#4 Deposit History Display all successful deposit amounts.
#5 Withdrawal History Display all successful withdrawal amounts.
#6 Exit Leave the ATM menu and end the session.

s = 0
deposit_history = list()
withdraw_history = list()

for i in range(3):

    p = int(input("Enter the Password: "))

    if p == 123:

        while True:

            u = int(input("""
Choose one of the option number:
1. Deposit
2. Withdraw
3. Balance Enquiry
4. Deposit History
5. Withdrawal History
6. Exit
Enter your option: """))

            if u == 1:
                z = int(input("Deposit the amount: "))

                if z > 0:
                    s = s + z
                    deposit_history.append(z)
                    print("Amount deposited successfully")
                else:
                    print("Amount should be greater than 0")

            elif u == 2:
                x = int(input("Enter the amount to withdraw: "))

                if x > 0 and x <= s:
                    s = s - x
                    withdraw_history.append(x)
                    print("Amount withdrawn successfully")
                else:
                    print("Invalid amount or insufficient balance")

            elif u == 3:
                print("Available Balance is:", s)

            elif u == 4:
                print("Deposit History:")
                print(deposit_history)

            elif u == 5:
                print("Withdrawal History:")
                print(withdraw_history)

            elif u == 6:
                print("Thank you for using the ATM")
                break

            else:
                print("Invalid option")

        break

    else:
        print("Try Again")

        if i >= 2:
            print("Out of Attempts")
```
