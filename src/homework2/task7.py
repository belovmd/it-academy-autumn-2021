"""7. Даны: три стороны треугольника. Требуется: проверить,
 действительно ли это стороны треугольника.
 Если стороны определяют треугольник, найти его площадь.
 Если нет, вывести сообщение о неверных данных.

 КАК ПРОВЕРИМ:
 У треугольника сумма любых двух сторон должна быть больше третьей.
 Иначе две стороны просто "лягут" на третью и треугольника не получится. )
"""

print('Введите три стороны треугольника')
a = int(input('Введите сторону A: '))
b = int(input('Введите сторону B: '))
c = int(input('Введите сторону C: '))

if (a + b - c) > 0 and (b + c - a) > 0 and (c + a - b) > 0:
    p = (a + b + c) / 2  # полупериметр
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5  # непосредственно площадь треугольника
    print('Площадь треугольника равна', round(s, 3))
else:
    print('Вы ввели неверные данные')
