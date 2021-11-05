'''
Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner. (все станет проще когда мы изучим модули, getattr
и setattr)
a. runner() – все фукнции вызываются по очереди
b. runner(‘func_name’) – вызывается только функцию func_name.
c. runner(‘func’, ‘func1’...) - вызывает все переданные функции
'''


import my_func


def runner():
    print('a')
    my_func.fizzbuzz()
    my_func.cubes()
    my_func.pairs()


runner()


def runner(func_name):
    print('b')
    if hasattr(my_func, func_name):
        getattr(my_func, func_name)()
    else:
        print('Not found')


runner('fizzbuzz')


def runner(*args):
    for arg in args:
        if hasattr(my_func, arg):
            getattr(my_func, arg)()
        else:
            print('Not found')


runner('fizzbuzz', 'cubes', 'pairs')
