"""Пары элементов
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
Задачу поместите в файл task4.py в папке src/homework3.
"""

input_str = '1 23 34 2 47 5 0 0 1 0 2'
input_list = input_str.split()
print(input_list)

num_list = [int(i) for i in input_list]
print(num_list)

par_count = 0
for i in range(len(num_list) - 1):
    for j in range(i + 1, len(num_list)):
        if num_list[i] == num_list[j]:
            par_count += 1

print('Number of pairs:', par_count)
