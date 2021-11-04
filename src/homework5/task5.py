# Написать программу которая находит ближайшую степень двойки к введенному числу.
# 10(8), 20(16), 1(1), 13(16)

def nearest_power_of_two_bit(number):
    i = 1
    nearest_power = number
    while nearest_power != 1:
        nearest_power = nearest_power >> 1
        i += 1
    if abs(number - (2 ** (i - 1))) <= abs(number - 2 ** i):
        print(2 ** (i - 1))
    else:
        print(2 ** i)
    return


nearest_power_of_two_bit(10)
nearest_power_of_two_bit(20)
nearest_power_of_two_bit(1)
nearest_power_of_two_bit(13)
