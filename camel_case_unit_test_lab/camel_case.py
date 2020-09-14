
import re
pattern = re.compile(r'\W')


def main():
    display_banner()
    sentence = get_input()
    outputs = camelCase_convert(sentence)
    print_results(outputs)


def display_banner():
    '''Display program name in banner'''
    msg = 'AWESOME camelCaseGenerator PROGRAM'
    stars = '*' * len(msg)
    print(f'\n {stars} \n {msg} \n {stars}\n')


def get_input():
    new_variable = input('Please enter a sentence to convert: ')
    return new_variable


def camelCase_convert(sentence):
    word_split = sentence.strip().split(' ')
    variable_name = ''
    for i in range(len(word_split)):
        if i == 0:
            variable_name += word_split[i].lower()
        else:
            variable_name += word_split[i].capitalize()
    mo = pattern.search(variable_name)
    if mo is not None:
        return 'Warning: There may be an issue in created variable name'
    else:
        return variable_name


def print_results(converted_var):
    print(converted_var)


if __name__ == '__main__':
    main()