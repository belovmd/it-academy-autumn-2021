"""
Даны два натуральных числа. Вычислите их наибольший общий делитель
при помощи алгоритма Евклида (мы не знаем функции и рекурсию).
"""

number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))

while number1 != number2:
    if number1 > number2:
        number1 -= number2
    else:
        number2 -= number1
print(number2)
