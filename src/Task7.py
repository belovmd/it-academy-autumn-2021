"""Оглянемся назад. Числа
Даны два натуральных числа. Вычислите их наибольший общий делитель при помощи
алгоритма Евклида (мы не знаем функции и рекурсию).
"""


def evklid():
    a = int(input("Введите а: "))
    b = int(input("Введите b: "))
    if a > b:
        while a % b:
            c = a % b
            a, b = b, c
        return b
    else:
        while b % a:
            c = b % a
            b, a = a, c
        return b


if __name__ == '__main__':
    print(evklid())
