# Python Fundamentals - Workshop Assignment 1

wizard = "Wizard"
elf = "Elf"
human = "Human"
orc = "Orc"

wizard_hp = 70
elf_hp = 100
human_hp = 150
orc_hp = 200

wizard_damage = 150
elf_damage = 100
human_damage = 20
orc_damage = 120

dragon_hp = 300
dragon_damage = 50

while True:
    while True:
        print("1)   Wizard")
        print("2)   Elf")
        print("3)   Human")
        print("4)   Orc")
        print("5)   Exit game")
        option = input("Choose your character: ")
        if option == "1" or option.lower() == "wizard":
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        elif option == "2" or option.lower() == "elf":
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break
        elif option == "3" or option.lower() == "human":
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break
        elif option == "4" or option.lower() == "orc":
            character = orc
            my_hp = orc_hp
            my_damage = orc_damage
            break
        elif option == "5" or option.lower() == "exit":
            print("Exited the game")
            quit()
        else:
            print("Unknown character")

    print("You have chosen the character:", character)
    print("Health:", my_hp)
    print("Damage:", my_damage)

    while True:
        dragon_hp = dragon_hp - my_damage
        print("The", character, "damaged the Dragon!")
        print("The Dragon's hitpoints are now:", dragon_hp)
        if dragon_hp <= 0:
            print("The Dragon has lost the battle")
            break
        my_hp = my_hp - dragon_damage
        print("The Dragon strikes back at", character)
        print("The", character, "'s hitpoints are now:", my_hp)
        if my_hp <= 0:
            print("The", character, "has lost the battle")
            break

    print("Do you want to play again? (Yes / No)")
    answer = input(">>")

    answer_yes = ["Yes", "Y", "yes", "y"]
    answer_no = ["No", "N", "no", "n"]

    if answer in answer_yes:
        print("Let's play!")
        continue
    elif answer in answer_no:
        print("Ok, goodbye!")
        quit()
    else:
        print("Huh? Bye dude!")
        break
