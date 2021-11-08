""""1. Оформите решение задач из прошлых домашних работ в функции. Напишите функцию runner.
(все станет проще когда мы изучим модули, getattr и setattr)
a. runner() – все фукнции вызываются по очереди
b. runner(‘func_name’) – вызывается только функцию func_name.
c. runner(‘func’, ‘func1’...) - вызывает все переданные функции"""
import homework3_funcs
from inspect import getmembers
from inspect import isfunction


def runner(*args):
    if not args:
        func_list = getmembers(homework3_funcs, isfunction)
        for func in func_list:
            func_name = func[0]
            print(f'результат функции {func_name}:', getattr(homework3_funcs, func_name)(), sep='\n')
    for func_name in args:
        print(f'результат функции {func_name}:', getattr(homework3_funcs, func_name)(), sep='\n')


# runner()
# runner('fizzbuzz')
# runner('unique_elements', 'fizzbuzz')
