"""Города"""

"""Дан список стран и городов каждой страны. 
Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
В
ходные данные
Программа получает на вход количество стран N. Далее идет 
N строк, каждая строка начинается с названия страны, затем
идут названия городов этой страны. В следующей строке
записано число M, далее идут M запросов — названия
каких-то M городов, перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны, в котором
находится данный город.
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
Russia
"""

dct = {}
for i in range(int(input('Введите количество стран:'))):
    country_cities = input('Введите название страны и её города:').split()
    country, cities = country_cities[0], country_cities[1:]
    for x in cities:
        dct[x] = country
for y in range(int(input('Введите колличество городов:'))):
    print(dct[input('Введите название города:')])
