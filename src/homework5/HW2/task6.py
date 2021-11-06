"""Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины. Задача требует работать только с числами
(без конвертации числа в строку или что-нибудь еще)
"""


def palindrome():
    x = int(input('Введите число больше 0: '))
    input_dig = x
    reverse_dig = 0
    while x:
        last_dig = x % 10
        reverse_dig = reverse_dig * 10 + last_dig
        x = x // 10
    if input_dig != reverse_dig:
        print('Не палиндром')
    else:
        print('Палиндром')
    return print()
