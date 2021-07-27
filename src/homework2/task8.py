# Зарегистрируйтесь на одном (или нескольких) из сайтов:
# https://py.checkio.org/ , https://www.codewars.com, https://www.hackerrank.com/,
# https://acmp.ru И решите 1-5 задач уровня Elementary и advanced.
# Поместите 3 простых и 2 сложных задачи на Ваш выбор в пул реквест.
"""

https://py.checkio.org/en/mission/multiply-intro/

Write a function that will receive 2 numbers as input and it should return

the multiplication of these 2 numbers.

Input: Two arguments. Both are of type int

Output: Int.

"""


def multiple_two(a, b):
    return a * b


"""

https://py.checkio.org/en/mission/first-word-simplified/

You are given a string and you have to find its first word.

 This is a simplified version of the First Word mission, which can be solved later.

    The input string consists of only English letters and spaces.

    There aren’t any spaces at the beginning and the end of the string.

Input: A string.

Output: A string.

"""


def first_word(text: str) -> str:
    return text.split()[0]


"""

https://py.checkio.org/en/mission/acceptable-password-i/

You are at the beginning of a password series. Every mission is based on the previous one.

The missions that follow will become slightly more complex.

In this mission, you need to create a password verification function.

The verification condition is:

    the length should be bigger than 6.

Input: A string.

Output: A bool.

"""


def is_acceptable_password(password: str) -> bool:
    return len(password) > 6


"""

https://www.codewars.com/kata/514b92a657cdc65150000006/python

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.

The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number

passed in.

    Note: If the number is a multiple of both 3 and 5, only count it once.

    Also, if a number is negative, return 0(for languages that do have them)

"""


def calc_summary(number):
    if number <= 0:
        return 0
    summary = 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            summary += i
    return summary


"""

https://www.codewars.com/kata/54da5a58ea159efa38000836

Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

"""


def find_it(seq):
    for value in seq:
        if seq.count(value) % 2 != 0:
            return value
    return None
