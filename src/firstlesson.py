import glob
import re
import sys
from time import localtime

#1
print('Hello, world!')

#2
name = input('What is your name?\n')
print('Hi, %s.' % name)

#3
friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print("iteration {iteration} is {name}".format(iteration=i, name=name))

#4
parents, babies = (1, 1)
while babies < 100:
    print('This generation has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)

#5
def greet(name):
    print('Hello', name)
greet('Jack')
greet('Jill')
greet('Bob')

#6
for test_string in ['555-1212', 'ILL-EGAL']:
    if re.match(r'^\d{3}-\d{4}$', test_string):
        print(test_string, 'is a valid US local phone number')
    else:
        print(test_string, 'rejected')

#7
prices = {'apple': 0.40, 'banana': 0.50}
my_purchase = {
    'apple': 1,
    'banana': 6}
grocery_bill = sum(prices[fruit] * my_purchase[fruit]
                   for fruit in my_purchase)
print('I owe the grocer $%.2f' % grocery_bill)

#8
# This program adds up integers that have been passed as arguments in the command line
try:
    total = sum(int(arg) for arg in sys.argv[1:])
    print('sum =', total)
except ValueError:
    print('Please supply integer arguments')

#9
# indent your Python code to put into an email
# glob supports Unix style pathname extensions
python_files = glob.glob('*.py')
for file_name in sorted(python_files):
    print('    ------' + file_name)
    with open(file_name) as f:
        for line in f:
            print('    ' + line.rstrip())
    print()

#10
activities = {8: 'Sleeping',
              9: 'Commuting',
              17: 'Working',
              18: 'Commuting',
              20: 'Eating',
              22: 'Resting'}
time_now = localtime()
hour = time_now.tm_hour
for activity_time in sorted(activities.keys()):
    if hour < activity_time:
        print(activities[activity_time])
        break
else:
    print('Unknown, AFK or sleeping!')

#11
REFRAIN = '''
%d bottles of beer on the wall,
%d bottles of beer,
take one down, pass it around,
%d bottles of beer on the wall!
'''
bottles_of_beer = 9
while bottles_of_beer > 1:
    print(REFRAIN %
          (bottles_of_beer, bottles_of_beer, bottles_of_beer - 1))
    bottles_of_beer -= 1
