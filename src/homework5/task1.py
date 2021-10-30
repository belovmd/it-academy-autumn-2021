from inspect import isfunction
from inspect import getmembers
import task1a


# runner
def runer():
    task1a.slova()
    task1a.strany()
    task1a.chisla()
    task1a.totalcost()
    task1a.spicok()
    task1a.generatot()
    task1a.delitel()
    task1a.chisla2()
    task1a.longestword()
    task1a.spacefreestring()
    task1a.fibonachi()
    task1a.listpractice()


runer()


# runner('func_name')
def runner2():
    call_function = input('Введите имя функции для вызова: ')
    if hasattr(task1a, call_function):
        getattr(task1a, call_function)()
    else:
        print('Нет функции {} в объекте {}'.format(call_function, task1a))


runner2()


# runner('func1', 'func2'...)
def runner3(*args):
    function_list = [element[0] for element in getmembers(task1a) if isfunction(element[1])]
    if args:
        function_list = args

    for element in function_list:
        if hasattr(task1a, element):
            getattr(task1a, element)()


runner3('slova', 'spicok')
