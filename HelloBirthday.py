'''
Thomas Mullins
8/25/2020
Description: This program will ask the user for their name and date of birth and provide feedback
including a personalized greeting, how many letters they have in their name, and a happy birthday message if they
were born in January
'''

def main():
    userName, birthMonth = inputs()
    nameNum, celebrate = processing(userName, birthMonth)
    outputs(userName, nameNum, celebrate)

def inputs():
    print('Hello, birthday month!')
    userName = input("What is your name, friend? ")
    birthMonth = input("What month were you born in? ")
    return userName, birthMonth

def processing(name, birth):
    nameNum = len(name)
    celebrate = ''
    if birth.lower() == "August":
        celebrate = True
    return nameNum, celebrate

def outputs(userName, nameNum, celebrate):
    print(f'Very nice to meet you {userName}!\nIf you were curious you have {nameNum} characters in your name!')
    if celebrate == True:
        print("And it looks like you have a birthday in August... Happy birthday!")



main()