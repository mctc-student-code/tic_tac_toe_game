from dataclasses import dataclass

@dataclass
# opposed to the 'traditional' version dataclasss require you to provide datatypes better for basic data that doesn't
# have to do much. FOr anything that requires other methods traditional should be used. does not require many
# boilerplate items
class Student:
    name: str
    college_id: int
    GPA: float

def main():
    # objects will require correct positional arguments to be created
    alice = Student('Alice', 12345, 3.45)
    bob = Student('Bob', 67890, 2.75)


    print(alice)
    print(bob)

main()