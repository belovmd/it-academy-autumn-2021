"""Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины. Задача требует работать только с числами
(без конвертации числа в строку или что-нибудь еще)
"""

x = int(input('Введите число больше 0: '))
# определяем разрядность введенного числа:

div = 1
while x / div >= 10:
    div = div * 10
# находим крайнюю левую и правую цифру:

while x > 0:
    left_dig = int(x // div)
    right_dig = x % 10
# сравниваем полученные значения, если они не равны, число не является палиндромом, прекращаем цикл:

    if left_dig != right_dig:
        print('Не палиндром')
        break
# если значения равны, перезаписываем исходное число, откидываем при этом крайние цифры,
# возвращаемся к проверке условия

    else:
        x = int((x % div) / 10)
        div = int(div / 100)
if not x:
    print('Палиндром')
