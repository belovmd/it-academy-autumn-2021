# Написать программу которая находит ближайшую степень двойки к введенному числу.
# 10(8), 20(16), 1(1), 13(16)

def nearest_power_of_two(n):
    i = 1
    while n >= 2 ** i:
        i += 1
    if abs(n - (2 ** (i - 1))) <= abs(n - 2 ** i):
        print(2 ** (i - 1))
    else:
        print(2 ** i)
    return


nearest_power_of_two(10)
nearest_power_of_two(20)
nearest_power_of_two(1)
nearest_power_of_two(13)
