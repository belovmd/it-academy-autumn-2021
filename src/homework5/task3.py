# Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел,
# отсортированных по возрастанию, которая этот список “сворачивает”
#  get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
#  get_ranges([4,7,10]) // "4,7,10"
#  get_ranges([2, 3, 8, 9]) // "2-3,8-9"


def get_ranges(range_list):
    string_from_list = str(range_list[0])
    result_list = []
    result_string = ''

    for i in range(1, len(range_list)):
        if range_list[i]-range_list[i-1] == 1:
            string_from_list += ('-' + str(range_list[i]))
        else:
            string_from_list += (',' + str(range_list[i]))
    string_from_list = string_from_list.split(',')

    for el in string_from_list:
        intermediate_string = el.split('-')
        if len(intermediate_string) >=2:
            result_list.append(intermediate_string[0] + '-' + intermediate_string[-1])
        else:
            result_list.append(el)

    for element in result_list:
        result_string += element + ', '
    return print(result_string[0:-2])


get_ranges([0, 1, 2, 3, 4, 7, 8, 10])
get_ranges([4, 7, 10])
get_ranges([2, 3, 8, 9])
