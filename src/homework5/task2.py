"""
Homework5 Task2
Создайте декоратор, который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы)
Задачу поместите в файл task2.py в папке src/homework5.
"""

import os.path


def dec(fun):
    all_sum = 0
    file_name = 'func_result.txt'
    check_file = os.path.exists(file_name)
    if check_file:
        with open(file_name, 'r') as f:
            all_sum = int(f.read())

    def wrapper():
        nonlocal all_sum
        all_sum += fun()
        with open(file_name, 'w') as f:
            f.write('%d' % all_sum)
        return all_sum
    return wrapper


@dec
def func():
    return 2


print(func())
print(func())
print(func())
