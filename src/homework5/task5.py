"""
   5. Написать программу которая находит ближайшую степень двойки
   к введенному числу. 10(8), 20(16), 1(1), 13(16)
   Задачу поместите в файл task5.py в папке src/homework5.
"""


a = int(input('Введите число: '))
x = a
bit_count = 0

if x > 0:
    while x > 0:
        x = x >> 1
        bit_count += 1
    real_pow = bit_count - 1
    small_two = 2 ** real_pow
    big_two = small_two << 1

    if abs(a - small_two) == abs(a - big_two):
        print('Ближайшие степени двойки', small_two, 'и', big_two,
              'равноудалены от введённого числа')
    elif abs(a - small_two) < abs(a - big_two):
        print('Ближайшая степень двойки к введённому числу:', small_two)
    else:
        print('Ближайшая степень двойки к введённому числу:', big_two)
else:
    print('Число должно быть больше нуля!')
