"""Города
Дан список стран и городов каждой страны. Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N. Далее идет N строк,
каждая строка начинается с названия страны, затем идут названия городов
этой страны. В следующей строке записано число M, далее идут M запросов —
названия каких-то M городов, перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны, в котором находится данный город.
Примеры

Входные данные
4
Russia Moscow Petersburg Novgorod Kaluga
France Brest Paris
Ukraine Kiev Donetsk Odessa
Belarus Minsk Brest

3
Odessa
Moscow
Novgorod

Выходные данные
Ukraine
Russia
Russia"""


def countries_cities():
    n = int(input("Введите количество стран: "))
    dict_ = {}
    for _ in range(n):
        inp = input("Введите страну и города через пробел: ").split()
        d = dict.fromkeys(inp[1:], inp[0])
        dict_.update(d)

    m = int(input("Введите количество городов: "))
    lst = []
    for _ in range(m):
        inp = input("Введите город: ")
        lst.append(inp)

    for city in lst:
        if city in dict_.keys():
            print(dict_[city])


if __name__ == '__main__':
    countries_cities()
