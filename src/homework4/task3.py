"""
3 Даны два списка чисел. Посчитайте, сколько различных чисел
содержится одновременно как в первом списке, так и во втором.
Задачу поместите в файл task3.py в папке src/homework4.
"""

list1 = [1, 2, 3, 4, 5, 6, 7, 0]
list2 = [1, 2, 3, 4, 5, 22, 12, 34, 106]

set1 = set(list1)
set2 = set(list2)

print(len(set1 & set2))
