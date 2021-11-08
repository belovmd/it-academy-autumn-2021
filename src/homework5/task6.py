"""6. Вводится число найти его максимальный делитель, являющийся степенью двойки.
10(2) 16(16), 12(4)."""


def nod(number):
    degree = 1
    while not number % degree:
        degree = degree << 1

    return degree >> 1


print(nod(10))
print(nod(18))
print(nod(12))
