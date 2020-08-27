
import re
import random
# regular expression pattern for validation
pattern = re.compile(r'[1-9]')
# dictionary used for game printing and validation on computer/player turn
game_square_dict = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9}
# used for turn tracking and winner announcement
turn = {'turn':'Player'}
game_playing = True


def main():
    # try:
        begin_game()
        print_board()
        while game_playing:
            user_turn()
            computer_turn()
    # except Exception as err:
    #     print(err)


# simple start for the user to see
def begin_game():
    print('Welcome to Tic-Tac-Toe!')
    input('Press enter to begin!')


# create and display game board
def print_board():
    print('{:<1}{:^1}{:<2}{:<1}{:^1}{:<2}{:<1}{:^1}{:<1}'.format('_', f'{game_square_dict[1]}', '_|','_', f'{game_square_dict[2]}', '_|','_', f'{game_square_dict[3]}', '_'))
    print('{:<1}{:^1}{:<2}{:<1}{:^1}{:<2}{:<1}{:^1}{:<1}'.format('_', f'{game_square_dict[4]}', '_|','_', f'{game_square_dict[5]}', '_|','_', f'{game_square_dict[6]}', '_'))
    print('{:<1}{:^1}{:<2}{:<1}{:^1}{:<2}{:<1}{:^1}{:<1}'.format(' ', f'{game_square_dict[7]}', ' |',' ', f'{game_square_dict[8]}', ' |',' ', f'{game_square_dict[9]}', ' \n'))


# ask user for entry during user turn, call for entry validation, call for win condition check
def user_turn():
    print('Player Turn!')
    num_selection = input('Choose an unoccupied square: ')
    square_choice = number_validation(num_selection)
    move_validation(square_choice)


def computer_turn():
    num_selection = random.randint(1,9)
    square_choice = number_validation(num_selection)
    move_validation(square_choice)


def win_condition():
    if turn['turn'] == 'Player':
        box = 'X'
    else:
        box = 'O'
    if (game_square_dict[1] == box and game_square_dict[2] == box and game_square_dict[3] == box):
        winner()
    elif (game_square_dict[4] == box and game_square_dict[5] == box and game_square_dict[6] == box):
        winner()
    elif (game_square_dict[7] == box and game_square_dict[8] == box and game_square_dict[9] == box):
        winner()
    elif (game_square_dict[1] == box and game_square_dict[4] == box and game_square_dict[7] == box):
        winner()
    elif (game_square_dict[2] == box and game_square_dict[5] == box and game_square_dict[8] == box):
        winner()
    elif (game_square_dict[3] == box and game_square_dict[6] == box and game_square_dict[9] == box):
        winner()
    elif (game_square_dict[1] == box and game_square_dict[5] == box and game_square_dict[9] == box):
        winner()
    elif (game_square_dict[3] == box and game_square_dict[5] == box and game_square_dict[7] == box):
        winner()

def winner():
    print(f"{turn['turn']} Wins!!!")
    again = input("Would you like to try again? Enter 'y' or 'n': ")
    while again.lower() != 'y' and again.lower() != 'n':
        again = input("Would you like to try again? Enter 'y' or 'n': ")
    if again == 'y':
        print()
        main()
    else:
        print('Thanks for playing!')
        exit()


def number_validation(selection):
    mo = pattern.search(str(selection))
    length = len(str(selection))
    while mo == None or length > 1:
        selection = input("Please enter a single number 1-9 with no spaces: ")
        mo = pattern.search(selection)
    regex = int(selection)
    return regex


def move_validation(choice):
    mo = pattern.search(str(game_square_dict[choice]))
    whosUp = turn['turn']
    if mo == None:
        if whosUp == 'Player':
            print('Not allowed, Choose an empty square')
            print_board()
            user_turn()
        elif whosUp == 'Computer':
            computer_turn()
    else:
        if whosUp == 'Player':
            game_square_dict[choice] = 'X'
            print_board()
            win_condition()
            turn['turn'] = 'Computer'
            print("Computer Turn!")
        elif whosUp == 'Computer':
            game_square_dict[choice] = 'O'
            print_board()
            win_condition()
            turn['turn'] = 'Player'


main()