"""Выведите n-ое число Фибоначчи, используя только временные переменные, циклические операторы
и условные операторы. n - вводится"""
n = int(input('Номер элемента в последовательности Фибоначчи: '))
early_num = current_num = 1
x = 0

while x < n - 2:
    current_num, early_num = early_num + current_num, current_num
    x += 1

print('Значение элемента n в последовательности Фибоначчи: ', current_num)
