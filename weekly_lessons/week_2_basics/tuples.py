cats = ('leopard', 'tiger', 'cheetah') # often use ()
birds = 'cardinal', 'robin', 'swan' #but you often don't have to

print(cats[0]) # index tuples like lists
print(cats[1:3]) # can slice tuples ('tiger', 'cheetah')

# Can't add or modify to a tuple once created

for bird in birds: # tuples can be looped
    print(bird)

# useful for returning multiple values from a function
def get_random_cat_and_pattern():
    return 'tiger', 'stripes' # returns a tuple

# Unpack your tuple to conventionally get both values in seperate variable
cat, pattern = get_random_cat_and_pattern() # cat = 'tiger', pattern = 'stripes

# if you prefer you can do this but it's usually morework
data = get_random_cat_and_pattern()
print(data[0])