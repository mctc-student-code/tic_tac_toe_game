import requests

question = input('Enter your question for the magic 8 ball: ')

magic_8_ball_url = f'https://8ball.delegator.com/magic/JSON/{question}'

try:
    response = requests.get(magic_8_ball_url).json()
    answer = response['magic']['answer']
    print(f'The magic 8 ball says....   {answer}')
except Exception as err:
    print('Sorry, can\'t ask the magic 8 ball. Are you connected to the internet?')
    print(err) # only do this while developing to help you debug

cats = ['lion', 'tiger', 'cheetah']

# print(cats[4]) # IndexError: list index out of range

try:
    print(cats[4])
except:
    print("that is not a valid list index")