from banking_pkg import account


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


while True:
    print("          == = Automated Teller Machine == =          ")
    user = input("Enter name to register: ")
    if len(user) > 9:
        print("The maximum name length is 10 characters.")
    else:
        break

while True:
    pin = input("Enter PIN: ")
    if len(pin) == 4 and pin.isdigit():
        balance = 0
        print(user, "has been registered with a starting balance of " +
              "$" + str(balance))
        break
    else:
        print("PIN must contain 4 numbers.")

print("\n          == = Automated Teller Machine == =          \nLOGIN")
while True:
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")
    if name_to_validate == user and pin_to_validate == pin:
        print("Login successful!")
        break
    else:
        print("Invalid credentials!")

while True:
    atm_menu(user)
    option = input("Choose an option: ")
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)
        print(f"Current Balance: ${balance:.2f}")
    elif option == "3":
        balance = account.withdraw(balance)
        print(f"Current Balance: ${balance:.2f}")
    elif option == "4":
        account.logout(user)
        break
    else:
        print("Invalid option")
