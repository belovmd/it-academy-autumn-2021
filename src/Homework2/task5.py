""" Выведите n-ое число Фибоначчи, используя только временные переменные,
циклические операторы и условные операторы. n - вводится"""

n = int(input('Ведите число:'))
a = 1
b = 1
i = 0
while i < n - 2:
    c = a + b
    a = b
    b = c
    i = i + 1
print('Число Фибоначи:', b)
