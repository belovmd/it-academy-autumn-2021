'''Пары элементов
    1. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
    Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
    Входные данные - строка из чисел, разделенная пробелами.
    Выходные данные - количество пар.
    Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
'''

str_ = '1 1 1 1'
lst = [int(_) for _ in str_.split()]
print(lst)
kol_par = 0
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] == lst[j]:
            kol_par += 1
print(kol_par)
