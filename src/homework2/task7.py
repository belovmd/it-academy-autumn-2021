'''Даны: три стороны треугольника. Требуется: проверить,
действительно ли это стороны треугольника.
Если стороны определяют треугольник, найти его площадь.
Если нет, вывести сообщение о неверных данных.
'''
a = int(input("1число"))
b = int(input("2число"))
c = int(input("3число"))
if (a + b) > c and (a + c) > b and (b + c) > a and a > 0 and b > 0 and c > 0:
    print("треугольник существует")
    p = (a + b + c) / 2
    square = (p * (p - a) * (p - b) * (p - c)) ** (0.5)
    print("его площадь равна", square)
else:
    print("треугольник не существует")
