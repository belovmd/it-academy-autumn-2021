"""
Дан список стран и городов каждой страны. Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N. Далее идет N строк, каждая строка начинается
с названия страны, затем идут названия городов этой страны. В следующей строке записано число M,
далее идут M запросов — названия каких-то M городов, перечисленных выше.
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
Russia
"""

# dct_ = {}
# country_amount = int(input('Input amount of countries: '))
# for i in range(country_amount):
#     country = input('Input country with cities: ')
#     lst_country = country.split(' ')
#     dct_loop = dict([(lst_country[0], lst_country[1:])])
#     dct_.update(dct_loop)
#
# city_amount = int(input('Input amount of requests: '))
# for i in range(country_amount):
#     city = input('Input required city: ')
#     for key, value in dct_.items():
#         for el in value:
#             if city == el:
#                 print(key)

motherland = {}
lst_ = []
for i in range(int(input('Введите колличество стран: '))):
    country, *cities = input('Введите страну и города: ').split()
    for city in cities:
        if not motherland[city]:
            motherland[city] = []
        motherland[city].append(country)
for i in range(int(input('Введите число запросов '))):
    a = motherland[input('Введите город ')]
    for country in a:
        print(country)
