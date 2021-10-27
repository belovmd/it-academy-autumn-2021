"""
Реализовать функцию get_ranges которая получает на вход непустой
список неповторяющихся целых чисел, отсортированных по возрастанию,
которая этот список “сворачивает”
get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
get_ranges([4,7,10]) // "4,7,10"
get_ranges([2, 3, 8, 9]) // "2-3,8-9
"""


def get_ranges(lst):
    leng = len(lst)
    jst_str = ""
    new_lst = []
    jst_str += str(lst[0])

    for num in range(leng - 1):
        if lst[num + 1] - lst[num] == 1:
            jst_str += '-' + str(lst[num + 1])
        else:
            jst_str += ',' + str(lst[num + 1])

    jst_str = jst_str.split(',')

    for i in jst_str:
        p = i.split("-")
        if len(p) >= 2:
            new_lst.append(p[0] + '-' + p[-1])
        else:
            new_lst.append(i)

    otvet = ''
    for el in new_lst:
        otvet += el + ', '
    return print(otvet[0:-2])


get_ranges([0, 1, 2, 3, 4, 7, 8, 10, 12, 14, 15])
# get_ranges([4, 7, 10,11,12,13,14,15, 25,26,28,30,31,32,55])
# get_ranges([2, 3, 8, 9])
