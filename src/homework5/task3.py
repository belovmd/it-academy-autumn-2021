'''Реализовать функцию get_ranges
    которая получает на вход непустой список неповторяющихся целых чисел,
    отсортированных по возрастанию, которая этот список “сворачивает”
    get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
    get_ranges([4,7,10]) // "4,7,10"
    get_ranges([2, 3, 8, 9]) // "2-3,8-9"
'''


def get_ranges(lst):
    result = []
    a = b = lst[0]  # a and b are range's bounds
    for element in lst[1:]:
        if element == b + 1:
            b = element
        else:
            result.append(str(a) if a == b else f'{a}-{b}')
            a = b = element
    result.append(str(a) if a == b else f'{a}-{b}')
    return result
