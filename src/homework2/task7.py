# Даны: три стороны треугольника. Требуется: проверить, действительно ли это стороны треугольника.
# Если стороны определяют треугольник, найти его площадь.
# Если нет, вывести сообщение о неверных данных.
from math import sqrt


def calc_square_triangle(a: float, b: float, c: float) -> float:
    p = (a + b + c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))


def is_triangle(a: float, b: float, c: float) -> bool:
    return a + b > c and a + c > b and c + b > a


if __name__ == '__main__':
    input_a = float(input("Input a: "))
    input_b = float(input("Input b: "))
    input_c = float(input("Input c: "))
    if is_triangle(input_a, input_b, input_c):
        print(f"Square is {calc_square_triangle(input_a, input_b, input_c)}")
    else:
        print("It is not triangle")
