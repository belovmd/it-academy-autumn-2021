# Даны: три стороны треугольника. Требуется: проверить,
# действительно ли это стороны треугольника.
# Если стороны определяют треугольник, найти его площадь.
# Если нет, вывести сообщение о неверных данных.

print('Please, enter the triangle sides in cm below: ')
side1 = int(input('First side: '))
side2 = int(input('Second one: '))
side3 = int(input('Third one: '))
if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    half_per = float((side1 + side2 + side3) / 2)
    triange_square = float(
        (
            (half_per * (half_per - side1) * (half_per - side2) * (half_per - side3))
        ) ** 0.5
    )
    print('Square is ', triange_square, 'square cm')
else:
    print('The triangle is not possible')
