print('Введите цену, которую Вы заплатили, за указанное количество товаров: ')
M=int(input('рублей: '))
N=int(input('копеек: '))
S=int(input('Введите приобретенное количество товара: '))
Rprice=M/S #цена одной штуки в рублях
Kprice=N/S # цена одной штуки в копейках
print('Цена за одну единицу составила: ', int(Rprice), 'рублей', int(Kprice), 'копеек')
L=int(input('Пожалуйста, введите желаемое количество товара: '))
#N1 - рассчитала копейки, чтобы сделать одно целое число
N1=N/100
price=M+N1 #сделала целое число
total= price/S*L
print('Общая цена товара за желаемое количество товаров составит: ',total, 'рублей')

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
    print ('Hello', name)

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

for activity_time in sorted(activities.keys()):
    if hour < activity_time:
        print (activities[activity_time])
        break
else:
    print ('Unknown, AFK or sleeping!')
"""task 11"""
REFRAIN = '''
%d bottles of beer on the wall,
%d bottles of beer,
take one down, pass it around,
%d bottles of beer on the wall!
'''
bottles_of_beer = 9
while bottles_of_beer > 1:
    print (REFRAIN % (bottles_of_beer, bottles_of_beer,
        bottles_of_beer - 1))
    bottles_of_beer -= 1
"""task 12"""
class BankAccount(object):
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def overdrawn(self):
        return self.balance < 0
my_account = BankAccount(15)
my_account.withdraw(50)
print (my_account.balance, my_account.overdrawn())
"""task 13"""
import unittest
def median(pool):
    copy = sorted(pool)
    size = len(copy)
    if size % 2 == 1:
        return copy[int((size - 1) / 2)]
    else:
        return (copy[int(size/2 - 1)] + copy[int(size/2)]) / 2
class TestMedian(unittest.TestCase):
    def testMedian(self):
        self.assertEqual(median([2, 9, 9, 7, 9, 2, 4, 5, 8]), 7)
if __name__ == '__main__':
    unittest.main()
"""task 14"""
def median(pool):
    '''Statistical median to demonstrate doctest.
    >>> median([2, 9, 9, 7, 9, 2, 4, 5, 8])
    6 #change to 7 in order to pass the test
    '''
    copy = sorted(pool)
    size = len(copy)
    if size % 2 == 1:
        return copy[int((size - 1) / 2)]
    else:
        return (copy[int(size/2 - 1)] + copy[int(size/2)]) / 2
if __name__ == '__main__':
    import doctest
    doctest.testmod()
"""task 15"""
from itertools import groupby
lines = '''
This is the
first paragraph.

This is the second.
'''.splitlines()
# Use itertools.groupby and bool to return groups of
# consecutive lines that either have content or don't.
for has_chars, frags in groupby(lines, bool):
    if has_chars:
        print (' '.join(frags))
# PRINTS:
# This is the first paragraph.
# This is the second.
"""task 16"""
import csv

# need to define cmp function in Python 3
def cmp(a, b):
    return (a > b) - (a < b)

# write stocks data as comma-separated values
with open('stocks.csv', 'w', newline='') as stocksFileW:
    writer = csv.writer(stocksFileW)
    writer.writerows([
        ['GOOG', 'Google, Inc.', 505.24, 0.47, 0.09],
        ['YHOO', 'Yahoo! Inc.', 27.38, 0.33, 1.22],
        ['CNET', 'CNET Networks, Inc.', 8.62, -0.13, -1.4901]
    ])

# read stocks data, print status messages
with open('stocks.csv', 'r') as stocksFile:
    stocks = csv.reader(stocksFile)

    status_labels = {-1: 'down', 0: 'unchanged', 1: 'up'}
    for ticker, name, price, change, pct in stocks:
        status = status_labels[cmp(float(change), 0.0)]
        print ('%s is %s (%.2f)' % (name, status, float(pct)))