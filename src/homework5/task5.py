# Написать программу которая находит ближайшую степень двойки
# к введенному числу. 10(8), 20(16), 1(1), 13(16)

def find_degree(num):
    degree = 1
    while degree < num:
        degree = degree << 1

    if degree - num < num - (degree >> 1):
        return degree
    else:
        return degree >> 1


print(find_degree(56))
print(find_degree(17))
