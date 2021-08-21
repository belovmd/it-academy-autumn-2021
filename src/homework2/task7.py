"""
Даны: три стороны треугольника. Требуется: проверить,
действительно ли это стороны треугольника.
Если стороны определяют треугольник, найти его площадь.
Если нет, вывести сообщение о неверных данных.
"""

sides = []
p = 0
sideAmount = 3
for i in range(sideAmount):
    sides.append(int(input("Введите сторону: ")))
    p += sides[i]
isTriangle = True

for i in range(sideAmount):
    if p - sides[i] <= sides[i]:
        isTriangle = False
        break
if isTriangle:
    p = p / 2
    print((p * (p - sides[0]) * (p - sides[1]) * (p - sides[2])) ** 0.5)
else:
    print("Это не треугольник")
