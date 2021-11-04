# Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел,
# отсортированных по возрастанию, которая этот список “сворачивает”
#  get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
#  get_ranges([4,7,10]) // "4,7,10"
#  get_ranges([2, 3, 8, 9]) // "2-3,8-9"

def get_ranges(lst):
    result = str(lst[0])
    for i in range(1, len(lst)):
        if lst[i - 1] + 1 == lst[i] and (i == len(lst) - 1 or lst[i] != lst[i + 1] - 1):
            result += '-' + str(lst[i])
        if lst[i - 1] + 1 != lst[i] != lst[i - 1] - 1:
            result += ',' + str(lst[i])
    return result


print(get_ranges([0, 3, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
