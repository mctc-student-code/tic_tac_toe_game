'''
Thomas Mullins
8/25/2020
Description: Program will ask the user to enter a sentence, and then return that sentence in camel case
'''

sentence = input('Please enter a sentence. Any sentence at all: ')
wordSplit = sentence.split(' ')
for i in range(len(wordSplit)):
    if i == 0:
        print(wordSplit[i].lower(), end='')
    else:
        print(wordSplit[i].capitalize(), end='')

