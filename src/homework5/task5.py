"""5. Написать программу которая находит ближайшую степень двойки к введенному числу.
10(8), 20(16), 1(1), 13(16)"""


def degree_2(number):
    degree = 1
    while degree < number:
        degree = degree << 1

    if degree - number > number - (degree >> 1):
        return degree >> 1
    else:
        return degree


print(degree_2(10))
print(degree_2(20))
print(degree_2(1))
print(degree_2(13))
