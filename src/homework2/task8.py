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
https://py.checkio.org/en/mission/first-word-simplified/
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
https://py.checkio.org/en/mission/acceptable-password-i/
'''


def is_acceptable_password(password: str) -> bool:
    return len(password) > 6
    return True


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))
    print("Coding complete? Click 'Check' to earn cool rewards!")


'''
Требуется вычислить факториал целого числа N. Факториал обозначают как N! и вычисляют по формуле:
N! = 1 * 2 * 3 * … * (N-1) * N, причем 0! = 1.
Так же допустимо рекуррентное соотношение: N! = (N-1)! * N
https://acmp.ru/index.asp?main=task&id_task=18
'''


n = int(input())

factorial = 1

for i in range(2, n + 1):
    factorial *= i

print(factorial)


'''
В нашем зоопарке появился заяц. Его поместили в клетку, и чтобы ему не было скучно,
директор зоопарка распорядился поставить в его клетке лесенку. Теперь наш зайчик может
прыгать по лесенке вверх, перепрыгивая через ступеньки. Лестница имеет определенное количество
ступенек N. Заяц может одним прыжком преодолеть не более К ступенек. Для разнообразия
зайчик пытается каждый раз найти новый путь к вершине лестницы. Директору любопытно,
сколько различных способов есть у зайца добраться до вершины лестницы при заданных значениях K и N.
Помогите директору написать программу, которая поможет вычислить это количество.
Например, если K=3 и N=4, то существуют следующие маршруты: 1+1+1+1, 1+1+2, 1+2+1,
2+1+1, 2+2, 1+3, 3+1. Т.е. при данных значениях у зайца всего 7 различных маршрутов
добраться до вершины лестницы.
https://acmp.ru/index.asp?main=task&id_task=11
'''


k, n = map(int, input().split())
d = [1] + [0] * n * k

for i in range(n):
    for j in range(1, k + 1):
        d[i + j] += d[i]

print(max(d))
