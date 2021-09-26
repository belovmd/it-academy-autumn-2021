"""Создайте декоратор, который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы)
Задачу поместите в файл task2.py в папке src/homework5.
"""


def my_decorator(fun):
    try:
        with open("N_times_function_called.txt", 'r') as f:
            i = int(f.read())
    except FileNotFoundError:
        i = 0

    def wrapper():
        nonlocal i
        i += fun()
        print(f"The function is called {i} times")
        with open("N_times_function_called.txt", 'w') as f:
            f.write(str(i))
        return i
    return wrapper


@my_decorator
def my_func():
    return 1


if __name__ == '__main__':
    print(my_func())
    print(my_func())
    print(my_func())
