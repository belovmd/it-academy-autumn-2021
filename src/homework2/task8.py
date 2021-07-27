"""
1.
Задача взята с сайта https://py.checkio.org/
Сложность задачи - Elementary+

Find the nearest value to the given one.
You are given a list of values as set form and a value 
for which you need to find the nearest one.
For example, we have the following set of numbers: 4, 7, 10, 11, 12, 17,
and we need to find the nearest value to the number 9. If we sort this
set in the ascending order, then to the left of number 9 will be number
7 and to the right - will be number 10. But 10 is closer than 7, which
means that the correct answer is 10.
A few clarifications:
If 2 numbers are at the same distance,
you need to choose the smallest one;
The set of numbers is always non-empty, i.e. the size is >=1;
The given value can be in this set, which means that it’s the answer;
The set can contain both positive and negative numbers,
but they are always integers;
The set isn’t sorted and consists of unique numbers.
Input: Two arguments. A list of values in the set form.
The sought value is an int.
Output: Int.
"""


def nearest_value(values: set, one: int) -> int:
    list_sort = sorted(list(values))
    found = list_sort[0]

    for i in list_sort:
        if abs(i - one) < abs(found - one):
            found = i

    return found


"""Проверка решения"""
"""
if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
"""


"""
2.
Задача взята с сайта https://py.checkio.org/
Сложность задачи - Elementary

For the input of your function, you will be given one sentence. 
You have to return a corrected version, that starts with a capital 
letter and ends with a period (dot).
Pay attention to the fact that not all of the fixes are necessary.
If a sentence already ends with a period (dot),
then adding another one will be a mistake.
Input: A string.
Output: A string.
Precondition: No leading and trailing spaces,
text contains only spaces, a-z A-Z , and .
"""


def correct_sentence(text: str):
    new_text = ''

    if text[0].islower():
        new_text += text[0].upper()
        new_text += text[1::]
    else:
        new_text = text

    if new_text[-1] != '.':
        new_text += '.'

    return new_text


"""Проверка решения"""
"""if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."
    
    print("Coding complete? Click 'Check' to earn cool rewards!")
"""


"""
3.
Задача взята с сайта https://py.checkio.org/
Сложность задачи - Elementary

In a given text you need to sum the numbers while 
excluding any digits that form part of a word.
The text consists of numbers, spaces and letters 
from the English alphabet.
Input: A string.
Output: An int.
"""


def sum_numbers(text: str):
    sum_num = 0
    list_ = text.split()

    for i in list_:
        if i.isdigit():
            sum_num += int(i)

    return sum_num


"""Проверка решения"""
"""
if __name__ == '__main__':
    print("Example:")
    print(sum_numbers('hi'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_numbers('hi') == 0
    assert sum_numbers('who is 1st here') == 0
    assert sum_numbers('my numbers is 2') == 2
    assert sum_numbers('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 3755
    assert sum_numbers('5 plus 6 is') == 11
    assert sum_numbers('') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
"""

"""
4.
Задача взята с сайта https://py.checkio.org/
Сложность задачи - Simple

In this mission you should check if all elements in the given list are equal.
Input: List.
Output: Bool.
Precondition: all elements of the input list are hashable
"""


def all_the_same(elements: list):
    answer = False
    uniq_elements = set()

    for elem in elements:
        uniq_elements.add(elem)

    if len(uniq_elements) <= 1:
        answer = True

    return answer


"""Проверка решения"""
"""
if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
"""


"""
5.
Задача взята с сайта https://py.checkio.org/
Сложность задачи - Simple

Every true traveler must know how to do 3 things: fix the fire,find
the water and extract useful information from the nature around him.
Programming won't help you with the fire and water, but when it
comes to the information extraction - it might be 
just the thing you need.
Your task is to find the angle of the sun above the horizon knowing the
time of the day. Input data: the sun rises in the East at 6:00 AM, which
corresponds to the angle of 0 degrees. At 12:00 PM the sun reaches its
zenith, which means that the angle equals 90 degrees.
6:00 PM is the time of the sunset so the angle is 180 degrees.
If the input will be the time of the night
(before 6:00 AM or after 6:00 PM), your function
should return - "I don't see the sun!".
"""


def sun_angle(time: str):
    answer = "I don't see the sun!"
    tim = time.split(':')
    hour = float(tim[0])
    minutes = float(tim[1])

    if 6 <= hour < 18 or hour == 18 and minutes == 0:
        answer = ((hour - 6) * 60 + minutes) * 0.25

    return answer


"""Проверка решения"""
"""
if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
"""
