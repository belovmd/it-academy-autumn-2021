"""
1 Оформите решение задач из прошлых домашних работ в функции.
  Напишите функцию runner. (все станет проще когда мы изучим модули, getattr и setattr)
a runner() – все фукнции вызываются по очереди
b runner(‘func_name’) – вызывается только функцию func_name. 
c runner(‘func’, ‘func1’...) - вызывает все переданные функции 
  Задачу поместите в файл task1.py в папке src/homework5.
"""

import fun_lib

def runner():
    print()
    print('Работает runner()! вызов нескольких функций внутри:')
    fun_lib.hw4task1()
    fun_lib.hw3task3()
    fun_lib.hw3task4()
    fun_lib.hw3task5()
    fun_lib.hw3task6()

runner()

def runner(func):
    print()
    print('Работает runner("func_name")! ***************')
    if hasattr(fun_lib, func):
        getattr(fun_lib, func)()
    else:
        print('Функция "', func, '" не найдена!')

runner('hw3task5')

def runner(*args):
    print()
    print('Работает runner("func", "func1"...)! ***************')
    for arg in args:
        if hasattr(fun_lib, arg):
            getattr(fun_lib, arg)()
        else:
            print('\n\nФункция "', arg, '" не найдена!')

runner('hw3task3', 'hw3task4', 'hw3task5')
