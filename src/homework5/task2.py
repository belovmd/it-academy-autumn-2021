"""
Создайте декоратор, который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы)
Задачу поместите в файл task2.py в папке src/homework5.
"""


def dec(func):
    def wrapper(arg1, arg2):
        result = func(arg1, arg2)
        fil = open('what_times.txt', 'a')
        fil.write(str(result) + '\n')
        fil.close()
    return wrapper


@dec
def my_func(a, b):
    sum_ = a + b
    return f'сумма ваших чисел: {sum_}'


my_func(412, 13)
