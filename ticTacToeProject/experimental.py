
import re
import random
# regular expression pattern for validation
pattern = re.compile(r'\b[1-9]\b')
# dictionary used for game printing and validation on computer/player turn
game_square_dict = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9}
# used for turn tracking and winner announcement
turn = {'turn':'Player'}
used_list = []
player = 'Player'
# manage game flow and performs exception handling
def main():
    begin_game()
    print_board()
    turn_controller()
    restart()


def turn_controller():
    validated_entry = new_turn()
    add_to_game_board(validated_entry)
    is_win_condition()


# simple start for the user to see
def begin_game():
    print('Welcome to Tic-Tac-Toe!')
    input('Press enter to begin!')


# create and display game board, game_square_dict is used for values on the board and updates as moves are made
def print_board():
    print('{:<1}{:^1}{:<2}{:<1}{:^1}{:<2}{:<1}{:^1}{:<1}'.format('_', f'{game_square_dict[1]}', '_|','_', f'{game_square_dict[2]}', '_|','_', f'{game_square_dict[3]}', '_'))
    print('{:<1}{:^1}{:<2}{:<1}{:^1}{:<2}{:<1}{:^1}{:<1}'.format('_', f'{game_square_dict[4]}', '_|','_', f'{game_square_dict[5]}', '_|','_', f'{game_square_dict[6]}', '_'))
    print('{:<1}{:^1}{:<2}{:<1}{:^1}{:<2}{:<1}{:^1}{:<1}'.format(' ', f'{game_square_dict[7]}', ' |',' ', f'{game_square_dict[8]}', ' |',' ', f'{game_square_dict[9]}', ' \n'))


# ask user for entry during user turn, call for entry validation, call for move validation
#TODO combine user_turn and computer turn using if/else to decide between routes. Return validated number
def new_turn():

    if turn['turn'] == 'Player':
        print('Player Turn!')
        num_selection = input('Choose an unoccupied square: ')
        valid_number = move_validation(number_validation(num_selection))
        return valid_number
    else:
        valid_number = move_validation(number_validation(random.randint(1, 9)))
        return valid_number


# conditional logic used to check for game winning combinations. When satisfied winner function called if not a draw
#TODO add else to call for user/computer turn method if no other conditions are met
def is_win_condition():

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
    elif len(used_list) == 9:
        print("Aaaand It's a tie!")
        # restart()
    else:
        if turn['turn'] == 'Player':
            turn['turn'] = 'Computer'
            turn_controller()
        else:
            player = 'Player'
            turn['turn'] = 'Player'
            turn_controller()


# print winner and call restart function
def winner():
    print(f"{turn['turn']} Wins!!!")
    restart()

# ask user if they would like to restart and resets the game board
def restart():
    again = input("Would you like to try again? Enter 'y' or 'n': ")
    while again.lower() != 'y' and again.lower() != 'n':
        again = input("Would you like to try again? Enter 'y' or 'n': ")
    if again == 'y':
        print()
        for i in range(len(game_square_dict)):
            game_square_dict[i+1]=i+1
        main()
    else:
        print('Thanks for playing!')
        exit()


# validation to ensure that only a single number 1-9 is entered
def number_validation(selection):
    mo = pattern.search(str(selection))
    while mo == None:
        selection = input("Please enter a single number 1-9 with no spaces: ")
        mo = pattern.search(selection)
    regex = int(selection)
    return regex


# checks game_square_dict if it is a number before allowing new assignment.
# after each accepted turn the win condition function is called
#TODO will use same basic format but will no longer be responsible for turn change or assignment to game_board
#TODO must return validated assignment
def move_validation(choice):
    mo = pattern.search(str(game_square_dict[choice]))
    whosUp = turn['turn']
    if mo == None:
        if whosUp == 'Player':
            print('Not allowed, Choose an empty square')
            print_board()
            new_turn()
        elif whosUp == 'Computer':
            new_turn()
    else:
        if whosUp == 'Player':
            used_list.append(choice)
            return choice
        elif whosUp == 'Computer':
            used_list.append(choice)
            return choice


def add_to_game_board(entry):
    whosUp = turn['turn']
    if whosUp == 'Player':
        game_square_dict[entry] = 'X'
        print_board()
    elif whosUp == 'Computer':
        game_square_dict[entry] = 'O'
        print_board()

main()