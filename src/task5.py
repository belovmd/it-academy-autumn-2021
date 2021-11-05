'''
Написать программу которая находит ближайшую степень двойки
к введенному числу. 10(8), 20(16), 1(1), 13(16)
'''


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
