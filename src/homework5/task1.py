''' Оформите решение задач из прошлых домашних работ в функции.
    Напишите функцию runner.
    runner() – все фукнции вызываются по очереди
    runner(‘func_name’) – вызывается только функцию func_name.
    runner(‘func’, ‘func1’...) - вызывает все переданные функции
'''


from inspect import getmembers, isfunction
import modul_for_hw5


def runner(*args):
    list_of_functions = [o[0] for o in getmembers(modul_for_hw5) if isfunction(o[1])]
    if args:
        for func in args:
            getattr(modul_for_hw5, str(func))()
    if not args:
        for elem in list_of_functions:
            getattr(modul_for_hw5, str(elem))()
