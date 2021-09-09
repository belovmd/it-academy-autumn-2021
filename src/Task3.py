"""Реализовать функцию get_ranges которая получает
на вход непустой список неповторяющихся целых чисел,
отсортированных по возрастанию, которая этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9" """


def get_ranges(lst):
    i, k = 1, 0
    l = len(lst)
    lst_global = []
    while i < l:
        if lst[i] - lst[i-1] != 1:
            lst_new = lst[k:i]
            lst_global.append([str(el) for el in lst_new])
            k = i
        i += 1
        if i == l:
            lst_new = lst[k:]
            lst_global.append([str(el) for el in lst_new])
    print(lst_global)
    str_1 = ", ".join(el[0] + "-" + el[-1] for el in lst_global if len(el) > 1)
    str_2 = ", " + ", ".join(el[0] for el in lst_global if len(el) == 1)
    str_global = str_1 + str_2
    print(str_global)


if __name__ == '__main__':
    a = [1, 2, 3, 5, 6, 7, 8, 9, 12, 13, 14, 18, 19, 24, 25, 26, 28, 30]
    get_ranges(a)
