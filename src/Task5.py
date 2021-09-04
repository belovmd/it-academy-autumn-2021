"""Языки
Каждый из N школьников некоторой школы знает Mi языков. Определите, какие языки знают
все школьники и языки, которые знает хотя бы один из школьников.
Входные данные
Первая строка входных данных содержит количество школьников N. Далее идет N чисел Mi,
после каждого из чисел идет Mi строк, содержащих названия языков, которые знает i-й школьник.
Пример входных данных:
3          # N количество школьников
2          # M1 количество языков первого школьника
Russian    # языки первого школьника
English
3          # M2 количество языков второго школьника
Russian
Belarusian
English
3
Russian
Italian
French

Выходные данные
В первой строке выведите количество языков, которые знают все школьники.
Начиная со второй строки - список таких языков. Затем - количество языков, которые знает
хотя бы один школьник, на следующих строках - список таких языков."""

from functools import reduce

def languages():
    n = int(input("Введите количество школьников: "))
    d_global = {}
    for i in range(1, n+1):
        s_local = set()
        m = int(input("Введите количество языков школьника: "))
        for k in range(1, m+1):
            language = input("Введите язык которым владеет школьник: ")
            s_local.add(language)
        d_global[i] = s_local

    set_1 = reduce((lambda x, y: x & y), [v for v in d_global.values()])

    lst_2 = []
    for v in d_global.values():
        lst_2 += list(v)

    dct = {}
    for element in lst_2:
        dct[element] = dct.get(element, 0) + 1

    lst_unique = [k for k, v in dct.items() if v == 1]

    print("Количество языков, которые знают все школьники: ")
    print(list(set_1), "=>", len(list(set_1)))
    print("Количество языков, которые знают хотя бы один школьник: ")
    print(lst_unique, "=>", len(lst_unique))


if __name__ == '__main__':
    languages()

