''' Решения задач из Homework3, преобразованные в функции.
'''

def task1():
    vivod = []
    for element in range(1, 101):
        if not element % 15:
            vivod.append('FizzBuzz')
        elif not element % 3:
            vivod.append('Fizz')
        elif not element % 5:
            vivod.append('Buzz')
        else:
            vivod.append(element)
    print(vivod)


def task2():
    lst1 = [i + k for i in 'ab' for k in 'bcd']
    print('1: ', lst1)

    lst2 = lst1[::2]
    print('2: ', lst2)

    lst3 = [elem + 'a' for elem in '1234']
    print('3: ', lst3)

    print('4: ', lst3.pop(1))

    lst3.insert(1, '2a')
    print('5: ', lst3)


def task3():
    lst = ['a', 'b', 'c']
    tpl = tuple(lst)
    print(tpl)

    tpl2 = ('a', 'b', 'c')
    lst2 = list(tpl2)
    print(lst2)

    a, b, c = 'a', 2, 'python'
    print(a, b, c)

    tpl4 = ((1, 2, 3), )
    print(len(tpl4))
    for elem in tpl4[0]:
        print(elem, end=' ')


def task4():
    lst = '1 1 1 1'.split()
    dct_ = {num: lst.count(num) for num in lst}
    couples = [sum(range(value)) for value in dct_.values()]
    print(sum(couples))


def task5():
    lst = [1, 0, 2, 5, 4, 7, 0, 1]
    new_lst = [elem for elem in lst if lst.count(elem) == 1]
    print('Уникальные элементы: ', new_lst)


def task6():
    str_ = input('Введите список целых чисел: ')
    lst = [int(_) for _ in str_.split()]
    new, new1 = [], []
    for elem in lst:
        if elem:
            new.append(elem)
        else:
            new1.append(elem)
    print(new + new1)
