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
# You are given a string and you have to find its first word.
# This is a simplified version of the First Word mission, which can be solved later.
# The input string consists of only English letters and spaces.
# There aren’t any spaces at the beginning and the end of the string.
# https://py.checkio.org/en/mission/first-word-simplified/

text = input()
a = text.split()
list(a)
print(a[0])

# TASK 3
# You should return a given string in reverse order.
# Input: A string.
# Output: A string.
# https://py.checkio.org/en/mission/backward-string/

string = str(input('Kindly input the string: '))
print(string[::-1])

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
    if x == '0':
        zero.append(x)
    else: break
print('The input number  begins with {} zeros.'.format(len(zero)))

# TASK 4
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
