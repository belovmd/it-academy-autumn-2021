"""Реализовать функцию get_ranges которая получает на вход
непустой список неповторяющихся целых чисел,
отсортированных по возрастанию, которая этот список “сворачивает"

get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
get_ranges([4,7,10]) // "4,7,10"
get_ranges([2, 3, 8, 9]) // "2-3,8-9"
”"""


def get_ranges(spicok):
    lst_ = []
    for i, y in enumerate(spicok):
        if spicok[i - 1] == y - 1:
            if spicok[i + 1] == y + 1:
                lst_.append('')
            else:
                lst_.append(' - {}'.format(y))
        else:
            lst_.append(', {}'.format(y))
    print((''.join(lst_)).lstrip(','))


get_ranges([1, 2, 3, 4, 5, 7, 8, 10])
get_ranges([4, 7, 10])
get_ranges([2, 3, 8, 9])
