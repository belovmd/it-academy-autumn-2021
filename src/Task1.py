"""Оформите решение задач из прошлых домашних работ в функции. Напишите функцию runner.
(все станет проще когда мы изучим модули, getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
Задачу поместите в файл task1.py в папке src/homework5.
"""

# from inspect import getmembers, isfunction

# from Homework3 import Task1, Task2, Task3, Task4, Task5, Task6


from Homework3.Task1 import crazy_function
# from Homework3.Task2 import *
# from Homework3.Task3 import *
from Homework3.Task4 import find_pairs
# from Homework3.Task5 import *
from Homework3.Task6 import sort_list

"""list_tasks = [Task1, Task2, Task3, Task4, Task5, Task6]
functions_list = [getmembers(t, isfunction) for t in list_tasks]
print(functions_list)"""


def runner(*args):
    result = ""
    for el in args:
        result += str(el()) + "\n" + "-" * 50 + "\n"
    return "Function result:\n" + result


func1 = runner(crazy_function)
func2 = runner(sort_list, crazy_function)
func3 = runner(sort_list, crazy_function, find_pairs)


if __name__ == '__main__':
    print(func1)
    print(func2)
    print(func3)
