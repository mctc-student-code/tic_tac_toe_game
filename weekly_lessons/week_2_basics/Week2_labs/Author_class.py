class Author:
    # creates new object
    def __init__(self, name):
        self.name = name
        self.books = []

    # used to add items to the books element list, using the argument as the title when called
    def publish(self, title):
        if title in self.books:
            print(f'"{title}" already exists in the library')
        else:
            self.books.append(title)

    # takes books list element and makes them readable as a string separated by a comma
    def __str__(self):
        titles = ', '.join(self.books) or "No published books"
        return f'{self.name} Books: {titles}'

def main():

    dick = Author('Phillip K. Dick')
    dick.publish('Do Androids Dream of Electric Sheep')
    dick.publish('A Scanner Darkly')
    dick.publish('A Scanner Darkly')
    print(dick)


main()