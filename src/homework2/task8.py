"""
You are going to be given a word. Your job is to return the middle character of the word.
If the word's length is odd, return the middle character. If the word's length is even,
return the middle 2 characters.
https://www.codewars.com/kata/56747fd5cb988479af000028/train/python
"""


def get_middle(s):
    if len(s) % 2:
        return s[len(s) // 2]
    else:
        return s[len(s) // 2 - 1] + s[len(s) // 2]


print(get_middle(input('Введите слово: ')))

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23. Finish the solution
so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
https://www.codewars.com/kata/514b92a657cdc65150000006/train/python
"""


def solution(number):
    out_number = 0
    for element in range(number):
        if not element % 3 or not element % 5:
            out_number += element
    return out_number


print(solution(int(input('Введите число: '))))

""" 
In this little assignment you are given a string of space separated numbers,
and have to return the highest and lowest number.
https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python
"""


def high_and_low(numbers):
    numbers = numbers.split(' ')
    max_val = max(numbers, key=lambda i: int(i))
    min_val = min(numbers, key=lambda i: int(i))
    numbers = f'{max_val} {min_val}'
    return numbers


print(high_and_low(input('Введите числа: ')))

""" 
Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.
https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
"""


def move_zeros(array):
    for element in ['(', ',', ')', '[', ']', '{', '}']:
        array = array.replace(element, '')
    array = array.split()

    for index, element in enumerate(array):
        if not int(element):
            array.pop(index)
            array.append(element)

    array = ', '.join(array)
    return array


print(move_zeros(input('Введите множество: ')))

""" 
Write a function that takes a string of parentheses, and determines if the order
of the parentheses is valid. The function should return true if the string is valid,
and false if it's invalid.
https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python
"""


def valid_parentheses(str_):
    for element in str_:
        if element not in ['(', ')', '[', ']', '{', '}', '>', '<']:
            str_ = str_.replace(element, '')

    for element in ['{}', '()', '[]', '<>']:
        while element in str_:
            str_ = str_.replace(element, '')

    if not str_:
        return True
    else:
        return False


print(valid_parentheses(input('Введите строку: ')))
