'''
Вводится число найти его максимальный делитель,
являющийся степенью двойки. 10(2) 16(16), 12(4).
'''


def divider(num):
    degree = 1

    while degree <= num:
        degree = degree << 1
    degree = degree >> 1

    while num % degree:
        degree = degree >> 1

    return degree


print(divider(20))
print(divider(18))
print(divider(56))
