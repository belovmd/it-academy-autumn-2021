'''Даны: три стороны треугольника. Требуется: проверить, действительно ли это стороны треугольника.
Если стороны определяют треугольник, найти его площадь.
Если нет, вывести сообщение о неверных данных.
'''
print('Please enter the triangle sides in cm below: ')
a = int(input('First side: '))
b = int(input('Second one: '))
c = int(input('Third one: '))
triangle1 = a + c
triangle2 = a + b
P = int((a + b + c) / 2)  # полупериметр
S = int(P * (P - a) * (P - b) * (P - c))
square = S ** (0.5)
if (a + b > c) and (a + c > b) and (b + c > a):
    print('Square is ', square)
else:
    print('The triangle is not possible')
