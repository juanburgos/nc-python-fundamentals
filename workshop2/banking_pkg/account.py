def show_balance(balance):
    print(f"Current balance: {balance:.2f}")


def deposit(balance):
    while True:
        amount = input("Enter amount to deposit: ")
        if amount != "0":
            if amount.isdigit() and float(amount) == abs(float(amount)):
                return float(balance) + float(amount)
            else:
                print("Invalid entry.")
        else:
            print("No zero (0) amounts")


def withdraw(balance):
    while True:
        amount = input("Enter amount to withdraw: ")
        if float(amount) < float(balance):
            if amount == "0":
                print("No zero (0) amounts.")
            elif amount.isdigit() and float(amount) == abs(float(amount)):
                return float(balance) - float(amount)
            else:
                print("Invalid entry.")
        else:
            print("Where are you going to get that kind of money?")


def logout(name):
    print("Goodbye", name + "!")
