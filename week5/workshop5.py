import random

# Task 1: Guess the number through user input


def guess_random_number(tries, start, stop):
    random_number = random.randint(start, stop)
    while tries != 0:
        print("Number of tries left:", tries)
        user_guess = input(f"Guess a number between {start} and {stop}:")
        if user_guess.isdigit():
            user_guess = int(user_guess)
            if user_guess < start or stop < user_guess:
                print("Come on, don't be funny! Try again.")
                tries -= 1
                if tries == 0:
                    print("You have failed to guess the number:", random_number)
                    break
            elif user_guess == random_number:
                print("You guessed the correct number!")
                break
            elif user_guess < random_number:
                print("Guess higher!")
                tries -= 1
            else:
                print("Guess lower!")
                tries -= 1
        else:
            print("Only numbers are valid.")


# Driver code for task 1
""" guess_random_number(5, 0, 10) """

# Task 2: Guess the number programmatically through linear search


def guess_random_num_linear(tries, start, stop):
    random_number = random.randint(start, stop)
    print("The number for the program to guess is:", random_number)
    for num in range(start, stop+1):
        print(
            f"Number of tries left {tries}\nThe program is guessing... {num}")
        if num != random_number:
            tries -= 1
            if tries == 0:
                print("The program has failed to guess the correct number")
                break
        else:
            print("The program has guessed the correct number!")
            break


# Driver code for task 2
""" guess_random_num_linear(5, 0, 10) """

# Task 3: Guess the number programmatically using binary search.


def guess_random_num_binary(tries, start, stop):
    random_number = random.randint(start, stop)

    lower_bound = start
    upper_bound = stop

    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound) // 2
        pivot_value = pivot

        if pivot_value == random_number:
            print("Found it!", random_number)
            break
        if pivot_value > random_number:
            upper_bound = pivot - 1
            tries -= 1
            if tries == 0:
                print("Your program failed to find the number")
                break
            print("Guessing lower!")
        else:
            lower_bound = pivot + 1
            tries -= 1
            if tries == 0:
                print("Your program failed to find the number")
                break
            print("Guessing higher!")


# Driver Code for task 3
""" guess_random_num_binary(5, 0, 100) """
