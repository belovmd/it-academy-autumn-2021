"""
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару, которую
необходимо посчитать. Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар. Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар.
"""


input_list = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]

dct = {}
for element in input_list:
    dct[element] = dct.get(element, 0) + 1

output_list = []
for number in dct.values():
    couple = sum(reversed(range(number)))
    output_list.append(couple)

print(output_list)
