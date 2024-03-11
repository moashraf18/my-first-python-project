# File name: CS112_A1_T2_3_20231136.py
# Purpose: Subtract a square game in Python. The user chooses the number of coins or we have 1000 coins. Each player takes a non-zero square number. Who takes the last wins.
# Author: Mohamed Ashraf Taha Abdellah
# ID: 20231136


# Some def which I will use later
# def for move for player 1
import math

def input_non_zero_square1():
    while True:
        try:
            move = int(input("Player1: Enter a non-zero square number (1, 4, 9, 16,…): "))
            if move <= 0:
                print("Please enter a number greater than zero: ")
                continue
            if math.sqrt(move) % 1 != 0:
                print("Please enter a non-zero square number: ")
                continue
            return move
        except ValueError:
            print("Please enter a valid non-zero square number: ")

# def for move for player 2
def input_non_zero_square2():
    while True:
        try:
            move = int(input("Player2: Enter a non-zero square number (1, 4, 9, 16,…): "))
            if move <= 0:
                print("Please enter a number greater than zero: ")
                continue
            if math.sqrt(move) % 1 != 0:
                print("Please enter a non-zero square number: ")
                continue
            return move
        except ValueError:
            print("Please enter a valid non-zero square number: ")

# def to check that the user enters a non-square number of coins
def is_square(number):
    sqrt = int(number ** 0.5)
    return sqrt ** 2 == number

def is_non_square(number):
    return not is_square(number)

def get_non_square_number():
    while True:
        try:
            user_input = int(input("Enter a non-square number: "))
            if user_input <= 0:
                print("Please enter a positive non-square number: ")
                continue
            if is_non_square(user_input):
                return user_input
            else:
                print("You entered a square number. Please enter a non-square number: ")
        except ValueError:
            print("Invalid input. Please enter a valid non-square number: ")

# Welcome message
print("                      Welcome to Subtract a square game!                     ")

# Information about the game
print("                                How to play?                                ")
print(" First : You choose whether you want to decide number of coins or it will be set as 1000.")
print(" Second : If you choose to decide number of coins ,you must choose a number which is non-square.")
print(" Third : You choose a non-zero square number of coins to remove.")
print(" Finally : Who takes the last coin wins the game ,knowing that the remaining of coins must be zero not a negative number.")
print("                                 Good luck!                                  ")
print('')
print('*******************************************************************')
print('')
# User choice
print("A) Choose number of coins? ")
print("B) Set number of coins to be 1000? ")
choice = input("Please select an option (A or B): ").strip().upper()
if choice == 'A':
    # Set number of coins
    n_coins = get_non_square_number()
    print("Number of coins = ", n_coins)

    # Start with player 1
    current_player = 1
    while n_coins > 0:
        if current_player == 1:
            move = input_non_zero_square1()
        else:
            move = input_non_zero_square2()

        # Ensure move doesn't make coins go negative
        if move > n_coins:
            print("Invalid move. You cannot take more coins than remaining!")
            continue

        n_coins -= move
        print(f'Now we have {n_coins}')
        if n_coins <= 0:
            print(f'Player {current_player} is winner')
            break

        # Switch player for the next turn
        current_player = 1 if current_player == 2 else 2
elif choice == 'B':
    # Set number of coins
    n_coins = 1000
    print('number of coins = 1000')

    # Start with player 1
    current_player = 1
    while n_coins > 0 and n_coins <= 1000:
        if current_player == 1:
            move = input_non_zero_square1()
        else:
            move = input_non_zero_square2()

        # Ensure move doesn't make coins go negative
        if move > n_coins:
            print("Invalid move. You cannot take more coins than remaining!")
            continue

        n_coins -= move
        print(f'Now we have {n_coins}')
        if n_coins <= 0:
            print(f'Player {current_player} is winner')
            break

        # Switch player for the next turn
        current_player = 1 if current_player == 2 else 2

# Here we make the user to choose if he wants to play again or to exit the game
while True:
    print('')
    print('*******************************************************************')
    print('')
    print("Do you want to play again?")
    print("A) Yes ")
    print("B) No ")
    choice = input("Please select an option (A or B): ").strip().upper()
    if choice == 'A':
        print("A) Choose number of coins? ")
        print("B) Set number of coins to be 1000? ")
        choice = input("Please select an option (A or B): ").strip().upper()
        if choice == 'A':
            # Set number of coins
            n_coins = get_non_square_number()
            print("Number of coins = ", n_coins)

            # Start with player 1
            current_player = 1
            while n_coins > 0:
                if current_player == 1:
                    move = input_non_zero_square1()
                else:
                    move = input_non_zero_square2()

                # Ensure move doesn't make coins go negative
                if move > n_coins:
                    print("Invalid move. You cannot take more coins than remaining!")
                    continue

                n_coins -= move
                print(f'Now we have {n_coins}')
                if n_coins <= 0:
                    print(f'Player {current_player} is winner')
                    break

                # Switch player for the next turn
                current_player = 1 if current_player == 2 else 2

        elif choice == 'B':
            # Set number of coins
            n_coins = 1000
            print('number of coins = 1000')

            # Start with player 1
            current_player = 1
            while n_coins > 0 and n_coins <= 1000:
                if current_player == 1:
                    move = input_non_zero_square1()
                else:
                    move = input_non_zero_square2()

                # Ensure move doesn't make coins go negative
                if move > n_coins:
                    print("Invalid move. You cannot take more coins than remaining!")
                    continue

                n_coins -= move
                print(f'Now we have {n_coins}')
                if n_coins <= 0:
                    print(f'Player {current_player} is winner')
                    break

                # Switch player for the next turn
                current_player = 1 if current_player == 2 else 2



    elif choice == 'B':
        print("Exiting the game. Thank you for playing!")
        break



