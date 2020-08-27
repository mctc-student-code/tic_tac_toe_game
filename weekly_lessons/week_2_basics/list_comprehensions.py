strings = ['pizza', 'Beyonce', 'cat']
lengths = []

for string in strings:
    length = len(string)
    lengths.append(length)

print(lengths)

'''
if you are making a list from another list, you can use list comprehensions'''

strings = ['pizza', 'Beyonce', 'cat']
lengths = [len(string) for string in strings]

print(lengths)

number_list = [1,40,300]
doubled_numbers = [n * 2 for n in number_list]
print(doubled_numbers) # [2, 80, 600]

number_list = [2,4,6]
number_plus_one = [n+1 for n in number_list]
print(number_plus_one)

'''
conditions may be added to filter a list
'''

numbers = [1, -10, 40, -6, -500, 350]
positive_numbers = [n for n in numbers if n >= 0]
print(positive_numbers) # [1, 40, 350]

foods = ['cheese pizza', 'pepperoni pizza', 'ice cream', 'veggie pizza', 'tacos']
pizzas = [food for food in foods if 'pizza' in food]
print(pizzas) # ['cheese pizza', 'pepperoni pizza', 'veggie pizza']

# python test for membership, is in operator
example = [1, 5, 10]
is_one_in_list = 1 in example # True
is_seven_in_list = 7 in example # False

course = 'ITEC 1150 Pregramming Logic'
if '1150' in course:
    print('This is Programming Logic')

practice_list = [0,3,4,0,22,1]
positive_numbers = [n for n in practice_list if n > 0]
print(positive_numbers)

courses = ['ITEC 2560', 'BTEC 1010', 'ITEC 2905']
itec_courses = [i for i in courses if 'ITEC' in i]
print(itec_courses)

'''
Combining filtering and operations
'''

foods = ['cheese pizza', 'pepperoni pizza', 'ice cream', 'veggie pizza', 'tacos']
pizzas = [food.upper() for food in foods if 'pizza' in food]
print(pizzas)

foods = ['cheese pizza', 'pepperoni pizza', 'ice cream', 'veggie pizza', 'tacos']
pizzas = []
for food in foods:
    if 'pizza' in food:
        uppercase_pizza = food.upper()
        pizzas.append(uppercase_pizza)
print(pizzas)

num_list = [0,10,4,0,32]
pos_number = [num * 2 for num in num_list if num > 0]
print(pos_number)

