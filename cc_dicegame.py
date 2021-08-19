import random

high_score = 0


def dice_game():
    global high_score

    while True:
        die_roll1 = random.randint(1, 6)
        die_roll2 = random.randint(1, 6)

        total = die_roll1 + die_roll2

        print("Current High Score:", high_score)
        print("1) Roll Dice")
        print("2) Leave Game")
        option = input("Enter your choice: ")
        if option == "1":
            print("You roll a...", die_roll1)
            print("You roll a...", die_roll2)
            print("\nYou have rolled a total of:", total)
            if high_score < total:
                high_score = total
                print("New high score!\n")
            else:
                print("Try to beat the high score\n")
        elif option == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid command")


dice_game()
