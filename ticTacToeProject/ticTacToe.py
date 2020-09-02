
import re
import random

# dictionary used for game printing and validation on computer/player turn
game_square_dict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
# used for turn tracking and winner announcement
turn = 'Player'
turn_count = 0
playing_game = True


# overarching controller. While loop is used for restart purposes and will loop through function calls until False is
# returned from the restart function. Else, break is used to end the loop and program normally.
def main():
    begin_game()
    while playing_game:
        print_board()
        game_winner = turn_controller()
        winner(game_winner)
        play_again = restart()
        if play_again is False:
            break

#TODO rewrite
# uses first while true loop to continue game until is_win_condition returns a boolean value.  Inner while loop is
# used so that Should move_validator() returns false the program will begin again to ensure number validation in the
# re-entry.
def turn_controller():
    while True:
        validated_entry = number_validation(new_turn())
        add_to_game_board(validated_entry)
        print_board()
        if is_win_condition():
            return is_win_condition()


# simple start for the user to see
def begin_game():
    print('Welcome to Tic-Tac-Toe!')
    input('Press enter to begin!')


# game board print statements use hard coded patterns for the layout. game_square dictionary is initially populated
# with numbers 1-9 and replaced by either "X" or "O" in the add_to_game_board function after numbers are selected and
# validated
def print_board():
    print('{:<1}{:^1}{:<2}{:<1}{:^1}{:<2}{:<1}{:^1}{:<1}'.format('_', f'{game_square_dict[1]}', '_|', '_',
                                                                 f'{game_square_dict[2]}', '_|', '_',
                                                                 f'{game_square_dict[3]}', '_'))
    print('{:<1}{:^1}{:<2}{:<1}{:^1}{:<2}{:<1}{:^1}{:<1}'.format('_', f'{game_square_dict[4]}', '_|', '_',
                                                                 f'{game_square_dict[5]}', '_|', '_',
                                                                 f'{game_square_dict[6]}', '_'))
    print('{:<1}{:^1}{:<2}{:<1}{:^1}{:<2}{:<1}{:^1}{:<1}'.format(' ', f'{game_square_dict[7]}', ' |', ' ',
                                                                 f'{game_square_dict[8]}', ' |', ' ',
                                                                 f'{game_square_dict[9]}', ' \n'))


# conditional logic is used to check which turn the game is on. If 'Player' is currently in the turn variable an
# input prompt will be used asking the player to select a number. If 'Computer' is currently stored in turn the
# random.randint function from the random library is used to choose a number 1-9. In either instance the number
# selected will be passed through the number_validation followed by the move_validation functions before being
# returned to the turn controller.
def new_turn():
    global turn
    if turn == 'Player':
        return input('Please choose an unoccupied square (1-9): ')
    else:
        return random.randint(1,9)

#TODO rewrite following comments
def number_validation(selection):
    global turn
    global turn_count
    pattern = re.compile(r'\b[1-9]\b')
    mo = pattern.search(str(selection))
    while mo is None or str(game_square_dict[int(selection)]).isnumeric() is False:
        if turn == "Player":
            selection = input("Not allowed. Please choose an unoccupied square: ")
            mo = pattern.search(selection)
        else:
            selection = random.randint(1,9)
    number_fixed = int(selection)
    if turn == 'Player':
        turn_count += 1
        return number_fixed
    elif turn == 'Computer':
        turn_count += 1
        return number_fixed


# entry parameter is used as the key to access an item in the game_square_dict dictionary. Dependant on value of turn,
# either an 'X' or 'O' will be assigned as the new value in the dictionary.
def add_to_game_board(entry):
    global turn
    if turn == 'Player':
        game_square_dict[entry] = 'X'
    elif turn == 'Computer':
        game_square_dict[entry] = 'O'


# turn variable is used to determine what value the conditional is looking for. Should any of the conditions be satisfied
# the program returns True to the turn controller and false if no matches are met but the game counter has reached 9
def is_win_condition():
    global turn
    if turn == 'Player':
        box = 'X'
    else:
        box = 'O'
    if (game_square_dict[1] == box and game_square_dict[2] == box and game_square_dict[3] == box) or \
            (game_square_dict[4] == box and game_square_dict[5] == box and game_square_dict[6] == box) or \
            (game_square_dict[7] == box and game_square_dict[8] == box and game_square_dict[9] == box) or \
            (game_square_dict[1] == box and game_square_dict[4] == box and game_square_dict[7] == box) or \
            (game_square_dict[2] == box and game_square_dict[5] == box and game_square_dict[8] == box) or \
            (game_square_dict[3] == box and game_square_dict[6] == box and game_square_dict[9] == box) or \
            (game_square_dict[1] == box and game_square_dict[5] == box and game_square_dict[9] == box) or \
            (game_square_dict[3] == box and game_square_dict[5] == box and game_square_dict[7] == box):
        return True
    elif turn_count == 9:
        return False
    # if no previous conditions are met, turn will be assigned a opposite of previous user and will be sent back to the
    # turn controller for the next round.
    else:
        if turn == 'Player':
            turn = 'Computer'
            print(f'{turn} turn')
        else:
            turn = 'Player'
            print(f'{turn} turn')


# game_win parameter to announce winner if game_win is True. Alternatively, a draw announcement is printed
def winner(game_win):
    if game_win:
        print(f"{turn} Wins!!!")
    else:
        print('It\'s a Draw!')


# User is asked to enter 'y' to play again. If condition is met a for loop is used to reset the game_square_dict to its
# original values and the counter is set back to 0 before the turn_controller is called to keep playing with the winner
# of the previous game starting. If n is entered a final message is printed and the program closes.
def restart():
    global turn_count
    again = input("Would you like to try again? Enter 'y' or 'n': ")
    while again.lower() != 'y' and again.lower() != 'n':
        again = input("Would you like to try again? Enter 'y' or 'n': ")
    if again == 'y':
        print()
        for i in range(len(game_square_dict)):
            game_square_dict[i + 1] = i + 1
        turn_count = 0
        return True
    else:
        print('Thanks for playing!')
        return False


main()