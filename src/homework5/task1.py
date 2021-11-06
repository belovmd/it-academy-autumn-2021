# Оформите решение задач из прошлых домашних работ в функции. Напишите функцию runner.
# (все станет проще, когда мы изучим модули, getattr и setattr)
# a. runner() – все фукнции вызываются по очереди
# b. runner(‘func_name’) – вызывается только функцию func_name.
# c. runner(‘func’, ‘func1’...) - вызывает все переданные функции
# любых домашних. идеальный вариант - универсальная функция, в которой вписан импортированный модуль
# (в нашем случае это импорт модуля с прошлыми задачами) и работать будет со всеми
# функциями из этого импортированного модуля
# создать можно как вышеупомянутым способом (что хорошо), так и поместив функции в сам файл решения,
# и работая только с ними (что не универсально)

import inspect
from inspect import getmembers
from inspect import isfunction

import previous_tasks


def runner(*args):
    if not args:
        functions_list = getmembers(previous_tasks, isfunction)
        func_names_list = []
        for func in functions_list:
            func_name = func[0]
            func_to_call = getattr(previous_tasks, func_name)
            func_names_list.append(func_to_call)

        runner_func_list(func_names_list)
    else:
        for func_name in args:
            getattr(previous_tasks, func_name)()


def runner_func_list(funcs):
    for func in funcs:
        func_to_call = getattr(previous_tasks, func.__name__)
        func_to_call_signature = inspect.signature(func_to_call)
        params = []
        if len(func_to_call_signature.parameters) != 0:
            for _ in func_to_call_signature.parameters:
                params.append(None)
        func_to_call(*params)


# runner()
# runner('palindrome')
# runner('palindrome', 'fibonacci_numbers')
