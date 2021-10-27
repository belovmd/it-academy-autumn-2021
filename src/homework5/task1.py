"""
Оформите решение задач из прошлых домашних работ в функции. Напишите функцию runner.
(все станет проще когда мы изучим модули, getattr и setattr)
a. runner() – все фукнции вызываются по очереди
b. runner(‘func_name’) – вызывается только функцию func_name.
c. runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""


def dct_gener():
    my_dct = {elem: elem ** 3 for elem in range(1, 21)}
    return print(my_dct)


def two_list():
    lst1 = [1, 3, 4, 5, 7, 8, 23, 11]
    lst2 = [3, 4, 5, 6, 8, 21, 11, 9]
    return print(len(set(lst1) & set(lst2)), 'различных чисел в списках')


def words():
    text = "just just  text \n for test test hey hi   pls work"
    lst = set(text.split())
    print('Различных слов -', len(lst))


list_func = (dct_gener, two_list, words)


def runner(*args):
    answ = ""
    if args:
        for func in args:
            answ += str(func())
    else:
        for func in list_func:
            answ += str(func())
    return answ

# runner()
# runner(two_list)
# runner(dct_gener, two_list)
