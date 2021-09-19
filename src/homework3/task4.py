"""Пары элементов
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
Задачу поместите в файл task4.py в папке src/homework3.
"""
import math


def f(n):
    return int(math.factorial(n) / (math.factorial(n - 2) * 2))

input_str = '1 23 34 7 2 47 5 0 0 1 0 2 7 7 3 7'
input_list = input_str.split()

num_list = [int(i) for i in input_list]
print(num_list)

set_ = set(num_list)

par_count = 0
k_elements = 0

for el in set_:
    k_elements = num_list.count(el)
    if k_elements > 2:
        par_count += f(k_elements)
    elif k_elements == 2:
        par_count += 1

print('Number of pairs:', par_count)
