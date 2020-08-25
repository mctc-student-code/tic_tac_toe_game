'''
Thomas Mullins
8/25/2020
Description: Program will ask the user for the names of the classes that they are taking, save them to a list,
and print all classes, one per line.
'''

classList = []
print('Welcome to the class list program')
classNum = input('How many classes are you taking? ')
while classNum.isnumeric() is False:
    classNum = input('Please enter only Numeric characters.\nHow many classes are you taking? ')
for i in range(int(classNum)):
    classInput = input(f'What is the name of class #{i+1}? ')
    classList.append(classInput)
print('\nYour Class List:')
for i in range(len(classList)):
    print(classList[i])

