"""Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner"""


# homework2, task1


def totalcost():
    m = int(input('Введите число рублей: '))
    kop = int(input('Введите число копеек: '))
    s = int(input('Введите количество товара: '))
    summa = f"Общая сумма: {s * m + (s * kop) // 100} рублей {s * kop % 100} копеек"
    print(summa)


# homework2, task2


def longestword():
    str_ = (input("Введите предложение: "))
    punktuation = [
        ',', '.', ':', ';', '- ', '!', '?', '(', ')', '[', ']', '{',
        '}', "'", '"', '$', '%', '^', '*', '&', '#', '№', '`', '~', '+',
        '/', '@', '_', '=', '>', '<'
    ]
    for mark in punktuation:
        str_ = str_.replace(mark, "")
    words = str_.split()
    long = max(words, key=len)
    print(long)


# homework2, task3


def spacefreestring():
    str_ = (input("Введите cтроку: "))
    new_str = ''
    for i in str_:
        if i not in new_str and i != ' ':
            new_str += i
    print(new_str)


# homework2, task4


def lettercoast():
    str_ = (input("Введите cтроку: "))
    let_s = 0
    let_b = 0
    for i in str_:
        if 'a' <= i <= 'z':
            let_s += 1
        else:
            if 'A' <= i <= 'Z':
                let_b += 1
    little = f'Колличество строчных букв:, {let_s}'
    big = f'Колличество прописных букв:, {let_b}'
    print(little, big)


# homework2, task5


def fibonachi():
    fibo = int(input("Введите n: "))
    f1 = 1
    f2 = 1
    for i in range(2, fibo):
        f1, f2 = f2, f1 + f2
    print(f2)


# homework2, task6


def palindrom():
    num = int(input("Введите число: "))
    n = num
    rnum = 0
    while n > 0:
        rnum = (rnum * 10) + (n % 10)
        n = n // 10
    if num == rnum:
        print(True)
    else:
        print(False)


# homework2, task 7


def triangle():
    a = int(input('Введите длину первой стороны: '))
    b = int(input('Введите длину второй стороны: '))
    c = int(input('Введите длину третьей стороны: '))
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    if a + b > c and a + c > b and b + c > a:
        print('Площадь треугольника', s)
    else:
        print('Введены неверные данные')


# homework3, task 1


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('FitzzBuzz')
        elif i % 3 == 0:
            print('Fitzz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


# homework3, task2


def listpractice():
    lst1 = [a + b for a in 'ab' for b in 'bcd']
    lst2 = lst1[::2]
    lst3 = [a + b for a in '1234' for b in 'a']
    lst4 = lst3.pop(1)
    lst5 = lst3[:]
    lst5.append('2a')
    print(lst2)
    print(lst4)
    print(lst5)


# homework3, task3


def typlepractice():
    lst = ['a', 'b', 'c']
    tpl = tuple(lst)
    print(tpl)
    tpl1 = ('a', 'b', 'c')
    lst1 = list(tpl1)
    print(lst1)
    a, b, c = ['a', 2, 'python']
    print(a, b, c)
    tpl2 = ('1, 2, 3',)
    print(len(tpl2))
    for i in tpl2:
        print(i)


# homework3, task4


def spicok():
    lst1 = [int(s) for s in input('Введите список чисел через пробел:').split()]
    counter = 0
    for element in range(len(lst1)):
        for element2 in range(element + 1, len(lst1)):
            if lst1[element] == lst1[element2]:
                counter += 1
    print(counter)


# homework3, task5


def spicok2():
    lst = input().split()
    lst1 = []
    for i in lst:
        if lst.count(i) == 1:
            lst1.append(i)
    print(*lst1)


# homework3, task6


def spicok3():
    lst = [int(i) for i in input('Введите список чисел: ').split()]
    for i in range(len(lst)):
        if not lst[i]:
            lst.append(lst.pop(i))
    print(*lst)


# homework4, task1


def generatot():
    dct_ = {int(element): element ** 3 for element in range(1, 21)}
    print(dct_)


# homework4, task2


def strany():
    motherland = {}
    for i in range(int(input('Введите колличество стран: '))):
        country, *cities = input('Введите страну и города: ').split()
        for city in cities:
            motherland[city] = country
    for i in range(int(input('Введите число запросов '))):
        print(motherland[input('Введите город ')])

# homework4, task3


def chisla():
    lst1 = [1, 2, 3, 4, 8, 5, 6, 7]
    lst2 = [1, 2, 6, 4, 5, 2, 3, 1, 6, 8, 3, 4, 5]
    set1, set2 = set(lst1), set(lst2)
    print('Колличество разных числел в списках: ', len(set1 & set2))

# homework5, task4


def chisla2():
    lst1 = [1, 2, 3, 4, 5, 100, 101, 102]
    lst2 = [1, 2, 3, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    set1, set2 = set(lst1), set(lst2)
    print('В первом списке:', len(set1 - set2), '\n''Во втором списке:', len(set2 - set1))


# homework5, tasl5


def std():
    students = int(input('Введите колличество школьников: '))
    language = []
    for i in range(students):
        lancost = int(input('Введите колличество языков школьника: '))
        sum_lan = set()
        for j in range(lancost):
            sum_lan.add(input('Введите язык: '))
        language.append(sum_lan)
    all_students = set.intersection(*language)
    some_students = set.union(*language)
    print('Колличество языков, которые знают все: ', len(all_students), *all_students, sep='\n')
    print('Знает хотя бы один: ', len(some_students), *some_students, sep='\n')


# homework4, task6


def slova():
    str_ = input('Введите строку: ').split()
    print(len(set(str_)))


# homework4, task7


def delitel():
    a = int(input('Введите  первое число: '))
    b = int(input('Введите второе число:'))
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    print('Наибольший общий делитель: ', a + b)
