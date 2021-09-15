import math

"""7. Даны: три стороны треугольника. Требуется: проверить,
действительно ли это стороны треугольника. Если стороны определяют треугольник,
найти его площадь. Если нет, вывести сообщение о неверных данных.
"""


def triangle(a, b, c):
    a = int(input("Значение стороны a:"))
    b = int(input("Значение стороны b:"))
    c = int(input("Значение стороны c:"))

    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return "Площадь треугольника %.3f" % s
    else:
        return "The triangle with you parameters doesn't exist!"


if __name__ == '__main__':
    a, b, c = '', '', ''
    print(triangle(a, b, c))
