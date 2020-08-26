'''
Thomas Mullins
8/25/2020
Description: Program will ask the user to enter a sentence, and then return that sentence in camel case
'''

import re
pattern = re.compile(r'\W')
sentence = input('Please enter a sentence. Any sentence at all: ')
wordSplit = sentence.split(' ')
variableName = ''
for i in range(len(wordSplit)):
    if i == 0:
        variableName += wordSplit[i]
        print(wordSplit[i].lower(), end='')
    else:
        variableName += wordSplit[i]
        print(wordSplit[i].capitalize(), end='')
mo = pattern.search(variableName)
if mo is not None:
    print(f'\nWarning: There may be an issue in created variable name "{variableName}"')

