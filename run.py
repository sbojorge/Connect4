"""
Modules used for writing the code of this project
"""
import random
from tabulate import tabulate
import pyfiglet
from colorama import (Fore, Back,
                      Style)


print(Fore.RED, pyfiglet.figlet_format('Connect 4', font='slant',
      justify='center'))
print(Style.RESET_ALL)

print("""Drop your letter in one of the 7 columns of the grid.
Be the first to get 4 in a row to win. If your opponent
is getting too close to 4 in a row, block him/her with
your own letter!\n""")

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
    Short introduction for interacting with the user
    """
    name = input("Hi, what's your name?: ")
    print(f'Welcome {name}! You are player 1 and your letter is R.')
    print("I am player 2 and my letter is Y. Let's play!\n")


def players_input():
    """
    Ask player for a column number to drop the letter and
    checks that input is valid
    """
    try:
        global computer
        global player
        computer = random.randint(0, 6)
        player = int(input('Please choose a column from 0-6: '))
        if player not in range(7):
            raise ValueError('Valid numbers for playing are 0-6.\n'
                             f'You entered {player}')
        else:
            print(f'Your choice is {player}\n'
                  f'My choice is {computer}.')
    except ValueError as e:
        print(f'Invalid data:{e} please enter a valid number.')


def display_choices_player():
    """
    Display player's position on the grid
    """
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

    create_board()


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


def play_game():
    """
    Main function for playing Connect 4
    """
    # welcome()
    # create_board()
    game_running = True
    while game_running:
        players_input()
        display_choices_player()
        display_choices_computer()


play_game()
