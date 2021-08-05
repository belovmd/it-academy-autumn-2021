# You are at the beginning of a password series. Every mission is based on the previous one.
# The missions that follow will become slightly more complex.
# In this mission, you need to create a password verification function.
# The verification condition is:
# the length should be bigger than 6.

password = input("Kindly input the password: ")
pass_length = len(password)   # defining the length of the pass
good = 6
if pass_length >= good:
    print('The password is strong enough')
else:
    print('The password is not strong, please change it.')

# You are given a string and you have to find its first word.
# This is a simplified version of the First Word mission, which can be solved later.
# The input string consists of only English letters and spaces.
# There aren’t any spaces at the beginning and the end of the string.

text = input()
a = text.split()
list(a)
print(a[0])
