# Вводится число найти его максимальный делитель,
# являющийся степенью двойки. 10(2) 16(16), 12(4).

def find_divider(num):
    degree = 1

    while degree <= num:
        degree = degree << 1
    degree = degree >> 1

    while num % degree:
        degree = degree >> 1

    return degree


print(find_divider(10))
print(find_divider(16))
print(find_divider(12))