"""
Дан список стран и городов каждой страны. Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.

Входные данные
Программа получает на вход количество стран N. Далее идет N строк,
каждая строка начинается с названия страны, затем идут названия городов этой страны.
В следующей строке записано число M, далее идут M запросов — названия
каких-то M городов, перечисленных выше.

Выходные данные
Для каждого из запроса выведите название страны, в котором находится данный город.


Пример:
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

q_of_countries = int(input('Введите количество стран: '))
countries = [input().split() for _ in range(q_of_countries)]
dct_of_countries = {element[0]: element[1:] for element in countries}

q_of_cities = int(input('Введите количество городов: '))
cities = [input() for _ in range(q_of_cities)]

for element in cities:
    for key, value in dct_of_countries.items():
        if element in value:
            print(key)

