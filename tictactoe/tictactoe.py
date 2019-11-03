"""
This is a tic tac toe game I made
"""

__author__ = 'Seamus Donnellan'

player_1 = input('Player 1, please put your name in: ')
player_2 = input('Player 2, please put your name in: ')\

board = [],[],[],[],[],[],[],[],[]

print(f"Hello {player_1}, and hello {player_2}, and welcome to tic tac toe!")


print(f'{player_1}, it is your go first.')
player_1_cross = input('Player 1, what do you want to be, X or O? ')
user_choice_1 = int(input('Where would you like to go? '))
user_choice_2 = ''

if user_choice_1 == 'O':
    user_choice_2 = 'X'
elif user_choice_1 == 'X':
    user_choice_2 = 'O'

