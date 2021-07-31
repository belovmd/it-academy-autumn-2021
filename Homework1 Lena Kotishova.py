# Task from the lesson
print('Пожалуйста, введите цену одной вещи ниже:')
M = int(input('рублей: '))
N = int(input('копеек: '))
S = int(input('Введите желаемое количество товара: '))
print('Цена одной вещи составила {0} рубля {1} копеек, посчитать {2} предмета'.format(M, N, S))
total_rubles = M * S
total_kopeck = N * S
while total_kopeck >= 100:
    total_kopeck = total_kopeck - 100
    total_rubles = total_rubles + 1
else:
    pass
print('Цена составит {} рублей {} копеек'.format(total_rubles, total_kopeck))

# 1 line: Output

print('Hello, world!')

# 2 lines: Input, assignment

name = input('What is your name?\n')
print('Hi, %s.' % name)

# 3 lines: For loop, built-in enumerate function, new style formatting

friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print("iteration {iteration} is {name}".format(iteration=i, name=name))

# 4 lines: Fibonacci, tuple assignment

parents, babies = (1, 1)
while babies < 100:
    print('This generation has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)

# 5 lines: Functions


def greet(name):


    print('Hello', name)
greet('Jack')
greet('Jill')
greet('Bob')

# 6 lines: Import, regular expressions

for test_string in ['555-1212', 'ILL-EGAL']:
    import re

    if re.match(r'^\d{3}-\d{4}$', test_string):
        print(test_string, 'is a valid US local phone number')
    else:
        print(test_string, 'rejected')

# 7 lines: Dictionaries, generator expressions

prices = {'apple': 0.40, 'banana': 0.50}
my_purchase = {
    'apple': 1,
    'banana': 6}
grocery_bill = sum(prices[fruit] * my_purchase[fruit]
                   for fruit in my_purchase)
print('I owe the grocer $%.2f' % grocery_bill)

# 8 lines: Command line arguments, exception handling.

try:
    import sys

    total = sum(int(arg) for arg in sys.argv[1:])
    print('sum =', total)

except ValueError:
    print('Please supply integer arguments')

# 18 lines: 8-Queens Problem (recursion)
BOARD_SIZE = 8


class BailOut(Exception):
    pass


def validate(queens):
    left = right = col = queens[-1]
    for r in reversed(queens[:-1]):
        left, right = left - 1, right + 1
        if r in (left, col, right):
            raise BailOut


def add_queen(queens):
    for i in range(BOARD_SIZE):
        test_queens = queens + [i]
        try:
            validate(test_queens)
            if len(test_queens) == BOARD_SIZE:
                return test_queens
            else:
                return add_queen(test_queens)
        except BailOut:
            pass
    raise BailOut
