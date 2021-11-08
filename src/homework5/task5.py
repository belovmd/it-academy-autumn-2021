''' Написать программу которая находит ближайшую степень двойки к введенному числу.
    10(8), 20(16), 1(1), 13(16)
'''


def two_in_power(num):
    power = 1
    while power < num:
        power = power << 1   
    if power - num < num - (power >> 1):
        return f'Ближайшая степень двойки: {power}'
    else:
        return f'Ближайшая степень двойки: {power >> 1}'
