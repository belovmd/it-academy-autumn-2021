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
