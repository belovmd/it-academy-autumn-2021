''' Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner. (все станет проще когда мы изучим модули, getattr
и setattr)
a. runner() – все фукнции вызываются по очереди
b. runner(‘func_name’) – вызывается только функцию func_name.
c. runner(‘func’, ‘func1’...) - вызывает все переданные функции '''


def text():
    a = "i love   Milk or   git or python"
    print(len(set(a.split())))


def qwe():
    lst = [0, 3, 8, 0, 0, 3, 2, 0]
    lst1 = [x for x in lst if x] + [0] * lst.count(0)
    print(lst1)


l_func = (text, qwe)


def runner(*args):
    a = ""
    if args:
        for func in args:
            a += str(func())
    else:
        for func in l_func:
            a += str(func())
    return a


runner(qwe)
