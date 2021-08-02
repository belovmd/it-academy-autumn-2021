"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes
cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.
"""
# password = 1257
# attempt = int(input('Enter your password: '))
# if password == attempt:
#     print('true')
# else:
#     print('false')


"""
You are going to be given a word. Your job is to return the middle character of the word.
If the word's length is odd, return the middle character. If the word's length is even,
return the middle 2 characters.
"""

# word = input('Enter your word: ')
# letters = len(word)
# if len(word) % 2:
#    middle = (letters // 2)
#    print(word[middle])
# else:
#    middle1 = ((letters // 2) - 1)
#    middle2 = (letters // 2)
#    print(word[middle1] + word[middle2])


"""
You will be given an array of numbers. You have to sort the odd numbers in ascending order
while leaving the even numbers at their original positions.
"""
list_ = [5, 4, 3, 8]
list_odd = []
list_even = []
list_new = []
for i in list_:
    if i % 2:
        list_odd.append(i)
        list_odd.sort()
    else:
        list_even.append(i)
for a in range(max(len(list_odd), len(list_even))):
    if a < len(list_odd):
        list_new.append(list_odd[a])
    if a < len(list_even):
        list_new.append(list_even[a])
print(list_, list_new)
