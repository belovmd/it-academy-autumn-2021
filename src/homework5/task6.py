# Вводится число найти его максимальный делитель, являющийся степенью двойки.
# 10(2) 16(16), 12(4).

def two_nearest_divisor(num):
    pow = 2
    multiples = [2, ]
    if num & 1:
        print('У числа нет делителя, являющегося степенью двойки')
    else:
        # create list of power of two
        for x in range(num):
            pow = (pow << 1)
            multiples.append(pow)
        for el in multiples:
            if not num % el:
                i = el
    return i


print(two_nearest_divisor(10))
