""" Выведите n-ое число Фибоначчи, используя только временные переменные,
    циклические операторы и условные операторы. n - вводится.
"""

number = int(input('Введите номер числа '))

element_1, element_2, element_3 = 1, 1, 0

if number == 1 or number == 2:
    print('Значение этого числа равно 1')
else:
    for _ in range(2, number):
        element_3 = element_1 + element_2
        element_1 = element_2
        element_2 = element_3
    print("Значение этого числа равно", element_3)
