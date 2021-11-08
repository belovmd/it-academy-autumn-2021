''' Вводится число найти его максимальный делитель, являющийся степенью двойки.
# 10(2) 16(16), 12(4).'''

def max_del(num):
    pow = 2
    multiples = [2, ]
    if num & 1:
        print('нет делителя')
    else:
        # create list of power of two
        for x in range(num):
            pow = (pow << 1)
            multiples.append(pow)
        for e in multiples:
            if not num % e:
                i = e
    return i


print(max_del(10))
