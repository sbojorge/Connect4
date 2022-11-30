"""
Modules used for writing the code of this project
"""
import random
from tabulate import tabulate
import pyfiglet
from colorama import (Fore, Back,
                      Style)


# For the grid of the game

row_0 = ["", "", "", "", "", "", ""]
row_1 = ["", "", "", "", "", "", ""]
row_2 = ["", "", "", "", "", "", ""]
row_3 = ["", "", "", "", "", "", ""]
row_4 = ["", "", "", "", "", "", ""]
row_5 = ["", "", "", "", "", "", ""]
rows = [row_0, row_1, row_2, row_3, row_4, row_5]
rows.reverse()


def create_board():
    """
    Using the tabulate module,prints the board for playing
    """
    global rows

    headers = [0, 1, 2, 3, 4, 5, 6]

    print(Back.BLACK, tabulate(rows, headers, tablefmt='grid',
          showindex='always'))
    print(Style.RESET_ALL)
    print('\n')


# Global variables
player = None
computer = random.randint(0, 6)


def welcome():
    """
    Ask user's name and check that it isn't an empty string.
    If it is, then raise an error until name is a valid
    input
    """
    name = None
    while not name:
        try:
            name = input("Hi, what's your name?: \n")
            if name == '':
                raise RuntimeError("Empty space isn't a name")
            else:
                print(f'Welcome {name}! You are player 1 and '
                      'your letter is R.')
                print("I am player 2 and my letter is Y. Let's play!\n")
                break
        except RuntimeError as e:
            print(f'Invalid data:{e} .')


def players_input():
    """
    Ask player for a column number to drop the letter and
    checks that input is valid
    """
    try:
        global computer
        global player
        computer = random.randint(0, 6)
        player = int(input('Please choose a column from 0-6: \n'))
        if player not in range(7):
            raise ValueError('Valid numbers for playing are 0-6.\n'
                             f'You entered {player}')
        else:
            print(f'Your choice is {player}\n'
                  f'My choice is {computer}')
    except ValueError as e:
        print(f'Invalid data:{e} please enter a valid number.')


def display_choices_player():
    """
    Display player's position on the grid
    """
    if player in range(7):
        if rows[5][player] == '':
            rows[5][player] = 'R'
        elif rows[4][player] == '':
            rows[4][player] = 'R'
        elif rows[3][player] == '':
            rows[3][player] = 'R'
        elif rows[2][player] == '':
            rows[2][player] = 'R'
        elif rows[1][player] == '':
            rows[1][player] = 'R'
        elif rows[0][player] == '':
            rows[0][player] = 'R'
        else:
            print('Tie!')
    else:
        print("Your current choice isn't valid")


def display_choices_computer():
    """
    Display computer's position on the grid
    """
    if rows[5][computer] == '':
        rows[5][computer] = 'Y'
    elif rows[4][computer] == '':
        rows[4][computer] = 'Y'
    elif rows[3][computer] == '':
        rows[3][computer] = 'Y'
    elif rows[2][computer] == '':
        rows[2][computer] = 'Y'
    elif rows[1][computer] == '':
        rows[1][computer] = 'Y'
    elif rows[0][computer] == '':
        rows[0][computer] = 'Y'
    else:
        print('Tie!')

    create_board()


def check_horizontal_win():
    """
    Check if there are 4 in a row
    """
    # check horizontal
    # Set row number
    row_number = 0
    # Outer loop so we can loop through each row
    for i in range(0, 5):
        # Inner loop to check each element in single list
        for j in range(0, len(row_0)+1):
            # Create a set if 4 are the same in a row
            # eval so we can use row_number variable
            check = set(eval(f"row_{row_number}[j-4:j]"))
            # Check is set is made and that set isn't matching 4 empty strings
            if len(check) == 1 and '' not in check:
                if 'R' in check:
                    print('PLAYER WINS')
                else:
                    print('COMPUTER WINS')
                    # Stop game
                # game_running = False
            # Increase row number
        row_number += 1


def check_vertical_win():
    """
    Checks for 4 in a column
    """


def check_diagonal_win():
    """
    Checks for 4 in a diagonal
    """


def play_game():
    """
    Main function for playing Connect 4
    """
    # create_board()
    # welcome()
    game_running = True
    while game_running:
        players_input()
        display_choices_player()
        display_choices_computer()
        check_horizontal_win()


play_game()
