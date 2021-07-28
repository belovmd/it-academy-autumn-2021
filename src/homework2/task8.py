'''
Зарегистрируйтесь на одном (или нескольких) из сайтов:
https://py.checkio.org/ , https://www.codewars.com,   https://www.hackerrank.com/,
https://acmp.ru И решите 1-5 задач уровня Elementary и advanced. Поместите 3 простых и 2
сложных задачи на Ваш выбор в пул реквест.
'''


'''
This is an intro mission, the purpose of which is to explain how to solve missions on CheckiO
and how to get the most out of solving them. When the mission is solved,
one more station becomes available for you, containing more complex missions.
So this mission is the easiest one. Write a function that will receive
2 numbers as input and it should return the multiplication of these 2 numbers.
Input: Two arguments. Both are of type int
Output: Int.
https://py.checkio.org/en/mission/multiply-intro/
'''


def mult_two(a, b):
    return a * b
    return None


if __name__ == '__main__':
    print("Example:")
    print(mult_two(3, 2))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert mult_two(3, 2) == 6
    assert mult_two(1, 0) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")


'''
You are given a string and you have to find its first word.
This is a simplified version of the First Word mission, which can be solved later.
The input string consists of only English letters and spaces.
There aren’t any spaces at the beginning and the end of the string.
Input: A string.
Output: A string.
'''


def first_word(text: str) -> str:
    return text.split()[0]
    return text[0:2]


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"
    print("Coding complete? Click 'Check' to earn cool rewards!")


'''
In this mission, you need to create a password verification function.
The verification condition is:
the length should be bigger than 6.
Input: A string.
Output: A bool.
'''


def is_acceptable_password(password: str) -> bool:
    return len(password) > 6
    return True


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))
    print("Coding complete? Click 'Check' to earn cool rewards!")
