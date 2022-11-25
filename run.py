"""
Modules used for writing the code of this project
"""
import random
from tabulate import tabulate
import pyfiglet


print(pyfiglet.figlet_format('Connect 4', font='slant', justify='center'))

print("""Drop your letter in one of the 7 columns of the grid.
Be the first to get 4 in a row to win. If your opponent
is getting too close to 4 in a row, block him/her with
your own letter!\n""")

player = None
computer = random.randint(0, 6)
game_running = True


def create_board():
    """
    Using the tabulate module,prints the board for playing
    """
    rows = [["", "", "", "", "", "", ""],
            ["", "", "", "", "", "", ""],
            ["", "", "", "", "", "", ""],
            ["", "", "", "", "", "", ""],
            ["", "", "", "", "", "", ""],
            ["", "", "", "", "", "", ""]]

    headers = [0, 1, 2, 3, 4, 5]

    print(tabulate(rows, headers, tablefmt='grid',
          showindex='always'))
    print('\n')

create_board()


def welcome():
    """
    Short introduction for interacting with the user
    """
    name = input("Hi, what's your name?: ")
    print(f'Welcome {name}! You are player 1 and your letter is R.')
    print("I am player 2 and my letter is Y. Let's play!\n")

welcome()
