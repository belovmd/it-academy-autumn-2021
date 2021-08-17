"""Даны: три стороны треугольника. Требуется: проверить, действительно ли это
стороны треугольника. Если стороны определяют треугольник, найти его площадь.
Если нет, вывести сообщение о неверных данных."""
a = int(input('сторона а:'))
b = int(input('сторона b:'))
c = int(input('сторона c:'))

if a + b > c and a + c > b and b + c > a:
    semi_perimeter = (a + b + c) / 2
    Square = (semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c)) ** 0.5
    print('Это треугольник, с площадью ', Square)
else:
    print('Это не треугольник')
