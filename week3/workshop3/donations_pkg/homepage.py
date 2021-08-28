def show_homepage():
    print("")
    print("      === DonateMe Homepage ===      ")
    print("-------------------------------------------")
    print("| 1.  Login       | 2.   Register         |")
    print("-------------------------------------------")
    print("| 3.  Donate      | 4.   Show Donations   |")
    print("-------------------------------------------")
    print("|             5.   Exit                   |")
    print("-------------------------------------------")


donations_to_add = []


def donate(username):
    donation_amt = float(input("Enter amount to donate: "))
    donations_to_add.append(donation_amt)
    donation = username + (f" donated ${donation_amt:.2f}")
    print("Thank you for your donation!")
    return donation


def show_donations(donations):
    print("\n--- All Donations ---")
    if donations == []:
        print("Currently, there are no donations.")
    else:
        for donation in donations:
            print(donation)
        print(f"Total: ${sum(donations_to_add):.2f}")
