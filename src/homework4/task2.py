"""2. Города
Дан список стран и городов каждой страны. Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N. Далее идет N строк, каждая строка начинается с
названия страны, затем идут названия городов этой страны. В следующей строке записано число M,
далее идут M запросов — названия каких-то M городов, перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны, в котором находится данный город.
Входные данные
4
Russia Moscow Petersburg Novgorod
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
n = int(input('Количество стран: '))
countries_and_cities_dct = {}

for _ in range(n):
    country, *cities = input('Страна и ее города: ').split()
    countries_and_cities_dct[country] = cities

m = int(input('Количество искомых городов: '))

for _ in range(m):
    city = input('Введите название искомого города: ')
    search_country = [key for key, value in countries_and_cities_dct.items() if city in value]
    print(*search_country)
