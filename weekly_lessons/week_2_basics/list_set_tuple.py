'''sets - unordered collection
duplicates not allowed'''

cats = {'Leaopard', 'Tiger', 'Cheetah'}
print(cats) # {'Leaopard', 'Cheetah', 'Tiger'}

for cat in cats:
    print(cat)

cats.add('Puma')
cats.remove('Cheetah')
print(cats) # {'Puma', 'Tiger', 'Leaopard'}

cats.add('Puma') # {'Puma', 'Tiger', 'Leaopard'} No duplicate

'''
Lists, sets, and tuples are all iterables
Can be looped, indexed, use len(), etc...'''

cat_tuple = tuple(cats)
cat_list = list(cats)
cat_set = set(cats)

cats = ['Tiger', 'Lion', 'Tiger', 'Cheetah', 'Lion', 'Cheetah', 'Puma']
cat_set = set(cats) # {'Lion', 'tiger', 'Puma', 'Tiger', 'CHeetah', 'Cheetah'}
cats_no_duplicates = list(cat_set)
print(cats_no_duplicates) # ['Puma', 'Tiger', 'Cheetah', 'Lion']
