'''Exception handling and context manager'''

try:
    # context manager; file will be automatically closed at the end of the code block
    # does NOT handle exceptions so the program will still crash
    with open('data.txt') as data_file:
        contents = data_file.read()
        print(contents)
except FileNotFoundError:
    print('File not found')


