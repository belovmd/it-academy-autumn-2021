# Реализовать функцию get_ranges которая получает на вход непустой список 
# неповторяющихся целых чисел, отсортированных по возрастанию,
# которая этот список “сворачивает”
#  get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
#  get_ranges([4,7,10]) // "4,7,10"
#  get_ranges([2, 3, 8, 9]) // "2-3,8-9"


def get_ranges(lst):
    for index, item in enumerate(lst):
        lst[index] = str(item)
    new_ranges = []
    for item in lst:
        if not new_ranges:
            new_ranges.append([item])
        elif int(int(item) - int(prev_item)) == 1:
            new_ranges[-1].append(item)
        else:
            new_ranges.append([item])
        prev_item = item

    return ['-'.join([el[0], el[-1]] if len(el) > 1 else el) for el in new_ranges]


ranges = [2, 3, 8, 9, 10, 11]

print(get_ranges(ranges))
