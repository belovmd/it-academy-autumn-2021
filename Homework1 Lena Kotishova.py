print('Введите цену, которую Вы заплатили, за указанное количество товаров: ')
M = int(input('рублей: '))
N = int(input('копеек: '))
S = int(input('Введите приобретенное количество товара: '))
Rprice = M / S  # цена одной штуки в рублях
Kprice = N / S  # цена одной штуки в копейках
print('Цена за одну единицу составила: ', int(Rprice), 'рублей', int(Kprice), 'копеек')
L = int(input('Пожалуйста, введите желаемое количество товара: '))
N1 = N / 100  # N1 - рассчитала копейки, чтобы сделать одно целое число
price = M + N1  #сделала целое число
total = price / S * L
print('Общая цена товара за желаемое количество товаров составит: ', total, 'рублей')
""" task 1"""
print('Hello, world!')
""" task 2"""
name = input('What is your name?\n')
print('Hi, %s.' % name)
""" task 3"""
friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print("iteration {iteration} is {name}".format(iteration=i, name=name))
"""task 4"""
parents, babies = (1, 1)
while babies < 100:
    print('This generation has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)
"""task 5"""


def greet(name):
    print('Hello', name)


greet('Jack')
greet('Jill')
greet('Bob')
"""task 6"""
import re
for test_string in ['555-1212', 'ILL-EGAL']:
    if re.match(r'^\d{3}-\d{4}$', test_string):
        print (test_string, 'is a valid US local phone number')
    else:
        print (test_string, 'rejected')
"""task 7"""
prices = {'apple': 0.40, 'banana': 0.50}
my_purchase = {
    'apple': 1,
    'banana': 6}
grocery_bill = sum(prices[fruit] * my_purchase[fruit]
                   for fruit in my_purchase)
print ('I owe the grocer $%.2f' % grocery_bill)
"""task 8"""
# This program adds up integers that have been passed as arguments in the command line
import sys
try:
    total = sum(int(arg) for arg in sys.argv[1:])
    print ('sum =', total)
except ValueError:
    print ('Please supply integer arguments')
"""task 9"""
# indent your Python code to put into an email
import glob
# glob supports Unix style pathname extensions
python_files = glob.glob('*.py')
for file_name in sorted(python_files):
    print ('    ------' + file_name)

    with open(file_name) as f:
        for line in f:
            print ('    ' + line.rstrip())

    print()
"""task 10"""
from time import localtime

activities = {8: 'Sleeping',
              9: 'Commuting',
              17: 'Working',
              18: 'Commuting',
              20: 'Eating',
              22: 'Resting' }

time_now = localtime()
hour = time_now.tm_hour


