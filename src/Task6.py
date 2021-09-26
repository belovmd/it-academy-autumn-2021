def max_divisor(x):
    b = x
    i = 0
    if x % 2:
        return None
    while not x % 2:
        x = x >> 1
        i += 1
    return 2**i


if __name__ == '__main__':
    print(max_divisor(88))
