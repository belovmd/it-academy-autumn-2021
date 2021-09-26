def two_power(x):
    b = x
    i = 0
    while x != 1:
        x = x >> 1
        i += 1

    if (2**(i+1) - b) > (b - 2**i):
        return f"{2**i} => {i}"
    else:
        return f"{2**(i+1)} => {i+1}"


if __name__ == '__main__':
    print(two_power(259))
