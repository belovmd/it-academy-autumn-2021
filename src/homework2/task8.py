# https://py.checkio.org/en/mission/first-word-simplified/
# This is a simplified version of the First Word mission, which can be solved later.
# The input string consists of only English letters and spaces.
# There aren’t any spaces at the beginning and the end of the string.
# Input: A string.
# Output: A string.

string = input()
string_lst = list(string.split())
print(string_lst[0])

# https://www.hackerrank.com/challenges/python-loops/problem
# Task
# The provided code stub reads and integer, n , from STDIN. For all non-negative integers i < n , print i  ** 2 .

n = int(input())
for i in range(0, n):
    print(i ** 2)

# https://www.hackerrank.com/challenges/py-if-else/problem
# Task
# Given an integer, , perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

n = int(input())
if n % 2:
    print("Weird")
elif 1 < n < 6:
    print("Not Weird")
elif 5 < n < 21:
    print("Weird")
elif n > 20:
    print("Not Weird")

# https://www.hackerrank.com/challenges/write-a-function/problem
# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function.
# It is only necessary to complete the is_leap function.

print("input year")
year = int(input())
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    print("leap year")
else:
    print("not a leap year")

# https://www.hackerrank.com/challenges/triangle-quest-2/problem
# You are given a positive integer N .
# Your task is to print a palindromic triangle of size N.
for i in range(1, int(input()) + 1):
    print(((10 ** i - 1) // 9) ** 2)
