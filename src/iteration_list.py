# 3 lines: For loop, built-in enumerate function, new style formatting
if __name__ == '__main__':
    friends = ['john', 'pat', 'gary', 'michael']
    for i, name in enumerate(friends):
        print("iteration {iteration} is {name}".format(iteration=i, name=name))
