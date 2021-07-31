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

word = input('Enter your word: ')
letters = len(word)
if len(word) % 2:
    middle = (letters // 2)
    print(word[middle])
else:
    middle1 = ((letters // 2) - 1)
    middle2 = (letters // 2)
    print(word[middle1] + word[middle2])
