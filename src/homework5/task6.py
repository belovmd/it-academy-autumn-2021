# Вводится число найти его максимальный делитель, являющийся степенью двойки.
# 10(2) 16(16), 12(4).

def max_divider(n):
    i = 0
    divider = 1
    while not n % divider:
        divider = divider << 1
        i += 1
    divider = 2 ** (i - 1)
    return print(divider)


max_divider(10)
max_divider(16)
max_divider(12)
