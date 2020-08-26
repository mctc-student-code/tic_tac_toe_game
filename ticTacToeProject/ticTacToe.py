
import re
import random
pattern = re.compile(r'[1-9]')
game_square_dict = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9}
num_list = [1,2,3,4,5,6,7,8,9]
turn = {'turn':0}

def main():
    begin_game()
    print_board()
    user_turn()

# simple start for the user to see
def begin_game():
    print('Welcome to Tic-Tac-Toe!')
    input('Press enter to begin!')
    return

# create and display game board
def print_board():
    print('{:<1}{:^1}{:<2}{:<1}{:^1}{:<2}{:<1}{:^1}{:<1}'.format('_', f'{game_square_dict[1]}', '_|','_', f'{game_square_dict[2]}', '_|','_', f'{game_square_dict[3]}', '_'))
    print('{:<1}{:^1}{:<2}{:<1}{:^1}{:<2}{:<1}{:^1}{:<1}'.format('_', f'{game_square_dict[4]}', '_|','_', f'{game_square_dict[5]}', '_|','_', f'{game_square_dict[6]}', '_'))
    print('{:<1}{:^1}{:<2}{:<1}{:^1}{:<2}{:<1}{:^1}{:<1}'.format(' ', f'{game_square_dict[7]}', ' |',' ', f'{game_square_dict[8]}', ' |',' ', f'{game_square_dict[9]}', ' '))

# ask user for entry during user turn, call for entry validation, call for win condition check, and call computer_turn method when finished
def user_turn():
    print('Player Turn!')
    num_selection = input('Choose an unoccupied square: ')
    square_choice = number_validation(num_selection)
    move_validation(square_choice)
    return

# runs computer turn and calls for win condition
def computer_turn():
    print("Computer Turn!")
    num_selection = input(random.choice(num_list))
    square_choice = number_validation(num_selection)
    move_validation(square_choice)
    return

def win_condition():
    return

def number_validation(selection):

    mo = pattern.search(selection)
    while mo == None or len(selection) > 1:
        selection = input("Please enter a single number 1-9 with no spaces: ")
        mo = pattern.search(selection)
    regex = int(selection)
    return regex

def move_validation(choice):
    mo = pattern.search(str(game_square_dict[choice]))
    whosUp = turn['turn']

    if mo == None:
        if whosUp == 0:
            print('Not allowed, Choose an empty square')
            print_board()
            user_turn()
        elif whosUp == 1:
            computer_turn()
    else:
        if whosUp == 0:
            turn['turn'] = 1
            game_square_dict[choice] = 'X'
            print_board()
            computer_turn()
        else:
            game_square_dict[choice] = 'O'
            turn['turn'] = 0
            print_board()
            user_turn()

    return

main()