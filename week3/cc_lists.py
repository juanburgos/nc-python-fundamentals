import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while len(diamonds) != 0:
    valid_characters = ["q", "Q"]
    option = input("Press enter to pick a card, or Q then enter to quit:")
    if option == option in valid_characters:
        break
    elif option == "":
        random_index = random.randint(0, len(diamonds) - 1)
        hand.append(diamonds[random_index])
        diamonds.pop(random_index)
        print("Your hand:", hand)
        print("Remaining cards:", diamonds)
        if diamonds == []:
            print("There are no more cards to pick.")
            break
    else:
        print("Invalid entry")
