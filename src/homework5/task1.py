# Оформите решение задач из прошлых домашних работ в функции.
# Напишите функцию runner. (все станет проще когда мы изучим модули, getattr и setattr)
# runner() – все фукнции вызываются по очереди
# runner(‘func_name’) – вызывается только функцию func_name.
# runner(‘func’, ‘func1’...) - вызывает все переданные функции

import function_for_task1


def runner(*args):
    if not args:
        function_for_task1.func_1()
        function_for_task1.func_2()
    else:
        for func_name in args:
            getattr(function_for_task1, func_name)()


runner()
print("\n")
runner('func_2')
print("\n")
runner('func_1', 'func_2')
