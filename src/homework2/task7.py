side1 = int(input('Введите длину первой стороны: '))
side2 = int(input('Введите длину второй стороны: '))
side3 = int(input('Введите длину третьей стороны: '))

if ((side2 - side3) < side1 < (side2 + side3) and
        (side1 - side3) < side2 < (side1 + side3) and
        (side1 - side2) < side3 < (side1 + side2)):
    p = (side1 + side2 + side3) / 2
    print(round(((p * (p-side1) * (p-side2) * (p-side3)) ** (1/2)), 2))
else:
    print('Данные неверны: это не треугольник.')
