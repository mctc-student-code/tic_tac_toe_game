#
# class Student:
#     # first argument to all class methods is self.
#     # refers to this instance of the object class
#     # within a class, all class properties are refferred to as self.property
#     def __init__(self, name, college_id, GPA):
#         self.name = name
#         self.college_id = college_id
#         self.GPA = GPA
#
#         # __str__ works like toString()
#     def __str__(self):
#         return f'Name: {self.name}, id: {self.college_id}, GPA: {self.GPA}'
#
# '''No need for getters and setters - attributes are public by default
# and can be accessed directly'''
#
# def main():
#     alice = Student('Alice', 'aa1234aa', 4.0)
#     bob = Student('Bob', 'bb1234bb', 2.7)
#
#     print(alice.name)
#     print(bob.college_id)
#     print(bob.GPA)
#
#     print(alice)
#     print(bob)
#
# '''Methods for Student class'''
#
#
# main()

# import random
#
# class Dice:
#     def __init__(self, sides=6):
#         self.sides = sides
#
#     def roll(self):
#         return random.randint(1, self.sides)
#
# def main():
#     dice = Dice()   # 6-sided dice
#
#     print(dice.roll())
#     print(dice.roll())
#
#     d20 = Dice(20)  #20-sided dice
#
#     for r in range(100):   # roll 100 times
#         print(d20.roll())
#
# main()

class Author:
    # creates new object
    def __init__(self, name):
        self.name = name
        self.books = []

    # used to add items to the books element list, using the argument as the title when called
    def publish(self, title):
        if title in self.books:
            print(f'{title} already exists in the library')
        self.books.append(title)

    # takes books list element and makes them readable as a string separated by a comma
    def __str__(self):
        titles= ', '.join(self.books) or "No published books"
        return f'{self.name}. Books: {titles}'

def main():

    dick = Author('Phillip K. Dick')
    dick.publish('Do Androids Dream of Electric Sheep')
    dick.publish('A Scanner Darkly')
    dick.publish('A Scanner Darkly')

    print(dick)

    tom = Author('Tom')
    print(tom)

main()

'''Dataclasses'''

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    college_id: int
    GPA: float

def main():

    alice = Student('Alice', 12345, 3.45)
    bob = Student('Bob', 67890, 2.75)

    print(alice)
    print(bob)

main()