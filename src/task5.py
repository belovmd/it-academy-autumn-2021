def degree(num):
    degree = 1
    while degree < num:
        degree = degree << 1

    if degree - num < num - (degree >> 1):
        return degree
    else:
        return degree >> 1


print(degree(18))
print(degree(98))
print(degree(115))
