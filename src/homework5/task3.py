"""3. Реализовать функцию get_ranges которая получает на вход непустой список
неповторяющихся целых чисел, отсортированных по возрастанию, которая этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_ranges(lst):
    new_lst = []
    prev_value = 0
    for value in lst:
        value = str(value)
        if not new_lst:
            new_lst.append([value])
        elif int(value) - int(prev_value) == 1:
            new_lst[-1].append(value)
        else:
            new_lst.append([value])
        prev_value = value

    return ['-'.join([elem[0], elem[-1]] if len(elem) > 1 else elem) for elem in new_lst]


a = get_ranges([0, 1, 2, 3, 4, 7, 8, 10])
# b = get_ranges([4, 7, 10])
# c = get_ranges([2, 3, 8, 9])
print(a)
