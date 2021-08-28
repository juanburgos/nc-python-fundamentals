from donations_pkg.homepage import show_donations, show_homepage, donate
from donations_pkg.user import login, register

database = {"admin": "password123"}
donations = []
authorized_user = ""
show_homepage()
if authorized_user == "":
    print("You must be logged in to donate.")
else:
    print("Logged in as:", authorized_user)

while True:
    option = input("Choose an option: ")
    if option == "1":
        username = input("Enter username: ").lower()
        password = input("Enter password: ").lower()
        authorized_user = login(database, username, password)
        show_homepage()
        print("Logged in as:", username)
    elif option == "2":
        while True:
            username = input("Enter username: ").lower()
            if len(username) > 10:
                print("Username cannot be over 10 characters.")
            else:
                break

        while True:
            password = input("Enter password: ").lower()
            if len(password) < 5:
                print("Password must be at least 5 characters.")
            else:
                break

        authorized_user = register(database, username)
        if authorized_user != "":
            database[username] = password

        show_homepage()
    elif option == "3":
        if authorized_user == "":
            print("\nYou are not logged in.")
        else:
            donation = donate(authorized_user)
            donations.append(donation)
        show_homepage()
    elif option == "4":
        show_donations(donations)
        show_homepage()
    elif option == "5":
        print("Leaving DonateMe...")
        break
    else:
        print("Invalid entry.")
