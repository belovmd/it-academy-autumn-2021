"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes
cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.
"""

attempt = (input('Enter your password: '))
if len(attempt) == 4 or len(attempt) == 6:
    print('true')
else:
    print('false')

"""
You are going to be given a word. Your job is to return the middle character of the word.
If the word's length is odd, return the middle character. If the word's length is even,
return the middle 2 characters.
"""

word = input('Enter your word: ')
wordLen = len(word)
if len(word) % 2:
    middle = (wordLen // 2)
    print(word[middle])
else:
    middle1 = ((wordLen // 2) - 1)
    middle2 = (wordLen // 2)
    print(word[middle1] + word[middle2])

"""
You will be given an array of numbers. You have to sort the odd numbers in ascending order
while leaving the even numbers at their original positions.
"""

str_ = input('Input array: ')
str_ = str_.strip()
str_ = str_.split(' ')
list_ = []

for char in str_:
    list_.append(int(char))

list_odd = []
list_even = []
list_new = []
for i in list_:
    if i % 2:
        list_odd.append(i)
    else:
        list_even.append(i)
list_odd.sort()
for a in range(max(len(list_odd), len(list_even))):
    if a < len(list_odd):
        list_new.append(list_odd[a])
    if a < len(list_even):
        list_new.append(list_even[a])
print(list_, list_new)

"""
Create a function that returns the sum of the two lowest
positive numbers given an array of minimum 4 positive
integers. No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.
"""

str_ = input('Input your number array: ')
str_ = str_.split()
array_ = []
for char in str_:
    array_.append(int(char))
array_.sort()
print(array_[0] + array_[1])


