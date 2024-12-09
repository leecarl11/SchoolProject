#declaring all the functions that's needed to run the cash machine application program
def show_balance(balance):
    print("***********************************")
    print(f"Your balance is £{balance: .2f}")
    print("***********************************")


def deposit():
    print("***********************************")
    amount = float(input("How much do you want to deposit? "))
    print("***********************************")
    if amount < 0:
        print("***********************************")
        print("Sorry,That's not a valid amount.")
        print("***********************************")
        return 0
    else:
        return amount


def withdraw(balance):
    print("***********************************")
    amount = float(input("How much do you want to withdraw? "))
    print("***********************************")
    if amount > balance:
        print("***********************************")
        print("Insufficient funds.")
        print("***********************************")
        return 0
    elif amount < 0:
        print("***********************************")
        print("Amount most be greater than zero.")
        print("***********************************")
        return 0
    else:
        return amount
def current_account(balance):
    print("***********************************")
    amount = float(input("current account balance. "))
    print("***********************************")
    if amount < 0:
        print(f"")


def invalid_transactions():
    print("Invalid Transactions")


def end():
    print("Exit")


def main():
    #balance variable
    balance = 0
    #boolean set to true while running or false will exit the program
    is_running = True
    #I placed most of the code within the while loop

    while is_running:
        print("***********************************")
        print("Cash machine simulation application")
        print("***********************************")
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Invalid transactions")
        print("5. Exit")
        print("***********************************")

        #choice variable for some user input
        choice = input("Enter your choice: 1-8: ")
        #checking to see the users choice by adding the if statement
        if choice == "1":
            #if choice is 1, then call the function to show_balance
            show_balance(balance)
        elif choice == "2":
            #if choice is 2, then call the function deposit
            balance += deposit()
        elif choice == "3":
            #if choice is 3, then call the function withdraw
            balance -= withdraw(balance)
        elif choice == "4":
            #if choice is 4, then call the function invalid_transactions
            invalid_transactions()
        elif choice == "5":
            #if choice is 5, then call the function exit
            is_running = False
    else:
        print("***********************************")
        print("Invalid choice")
        print("***********************************")

main()
print("***********************************")
print("Thank you! have a nice day! ")
print("***********************************")

