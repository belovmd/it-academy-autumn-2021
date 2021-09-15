"""Даны два списка чисел. Посчитайте, сколько различных чисел содержится
одновременно как в первом списке, так и во втором.
Задачу поместите в файл task3.py в папке src/homework4.
"""


def list_intersection():
    lst1 = [1, 3, 4, 6, 8, 98, 45, 34, 21, 46, 36, 4, 9, 7, 10]
    lst2 = [i for i in range(21)]
    set1, set2 = set(lst1), set(lst2)
    return (set1 & set2), "=>", len(set1 & set2)


if __name__ == '__main__':
    print(list_intersection())
