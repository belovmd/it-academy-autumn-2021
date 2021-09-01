# TASK 1
# You are at the beginning of a password series. Every mission is based on the previous one.
# The missions that follow will become slightly more complex.
# In this mission, you need to create a password verification function.
# The verification condition is: the length should be bigger than 6.
# https://py.checkio.org/en/mission/acceptable-password-i/

password = input("Kindly input the password: ")
pass_length = len(password)   # defining the length of the pass
good = 6
if pass_length >= good:
    print('The password is strong enough')
else:
    print('The password is not strong, please change it.')

# TASK 2
# https://www.codewars.com/kata/54da5a58ea159efa38000836
# Given an array of integers,
# find the one that appears an odd number of times.
# Examples
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] shold return 4, because it appears 1 time (which is odd).

array = [1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1]
for i in range(0, len(array)):
    count = 0
    for b in range(0, len(array)):
        if array[i] == array[b]:
            count += 1
    if count % 2 or count == 1:
        print(array[i])

# TASK 3
# The Western Suburbs Croquet Club has two categories of membership, Senior and Open.
# They would like your help with an application form that will tell prospective members
# which category they will be placed.
# To be a senior, a member must be at least 55 years old and have a handicap greater than 7.
# In this croquet club, handicaps range from -2 to +26;
# the better the player the lower the handicap.
# Input will consist of a list of lists containing two items each.
# Each list contains information for a single potential member.
# Information consists of an integer for the person's age and
# an integer for the person's handicap.


def candidates(candidates_list):
    candidates = []
    for i in candidates_list:
        if i[0] < 55 or i[1] < 7:
            candidates.append('Open')
        else:
            candidates.append('Senior')
    print(candidates)

# TASK 4
# You have a string that consist only of digits.
# You need to find how many zero digits ("0")
# are at the beginning of the given string.
# Input: A string, that consist of digits.
# beginning_zeros('001001') == 2
# beginning_zeros('0000') == 4

beginning_zeros = str(input('Number: '))
zero = []
for x in beginning_zeros:
    if x != '0':
        break
    else:
        zero.append(x)
print('The input number  begins with {} zeros.'.format(len(zero)))

# TASK 5
# Find the nearest value to the given one.
# You are given a list of values as set form
# and a value for which you need to find the nearest one.
# nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
# nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
# https://py.checkio.org/en/mission/nearest-value/

nearest_value = [int(i) for i in input('The list of the numbers: ').split()]
number = int(input('Number for checking: '))
nearest_value.sort()
found = nearest_value[0]
new_list = {}
for value in nearest_value:
    a = abs(number - value)
    if a < abs(number - found):
        found = value
print('The nearest to {} is {}'.format(number, found))
