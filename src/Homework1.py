# task 1
print('Hello, world!')

# task 2
name = input('What is your name?\n')
print('Hi, %s.' % name)

# task 3
friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print("iteration {iteration} is {name}".format(iteration=i, name=name))

# task 4
parents, babies = (1, 1)
while babies < 100:
    print('This generation has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)

# task 5


def greet(name):
    print('Hello', name)


greet('Jack')
greet('Jill')
greet('Bob')

# task 6
import re
for test_string in ['555-1212', 'ILL-LEGAL']:
    if re.match(r'^\d{3}-\d{4}$', test_string):
        print(test_string, 'is a valid US local phone number')
    else:
        print(test_string, 'rejected')
