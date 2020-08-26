'''
Thomas Mullins
8/25/2020
Description: This program will ask the user for their name and date of birth and provide feedback
including a personalized greeting, how many letters they have in their name, and a happy birthday message if they
were born in January
'''

# import datetime to check user birthday
from datetime import datetime

def main():
    userName, birthMonth = inputs()
    nameNum, celebrate = processing(userName, birthMonth)
    outputs(userName, nameNum, celebrate)

def inputs():
    # gather user input
    print('Hello, birthday month!')
    userName = input("What is your name, friend? ")
    birthMonth = input("What month were you born in? ")
    return userName, birthMonth

def processing(name, birth):
    # use len to get number of characters
    nameNum = len(name)
    # initialize celebrate variable
    celebrate = ''
    # conditional to see if user was born in current month using text format from datetime
    if birth.capitalize() == datetime.now().strftime('%B'):
        celebrate = True
    return nameNum, celebrate

def outputs(userName, nameNum, celebrate):
    # provide output to user and conditional message if it is their birth month
    print(f'Very nice to meet you {userName}!\nIf you were curious you have {nameNum} characters in your name!')
    if celebrate == True:
        print("And it looks like you have a birthday in August... Happy birthday!")



main()