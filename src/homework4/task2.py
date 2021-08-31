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

dct_ = {}
country_amount = int(input('Input amount of countries: '))
while country_amount > 0:
    country = input('Input country with cities: ')
    lst_country = country.split(' ')
    dct_loop = dict([(lst_country[0], lst_country[1:])])
    dct_.update(dct_loop)
    country_amount -= 1
print(dct_.keys())

city_amount = int(input('Input amount of requests: '))
while city_amount > 0:
    city = input('Input required city: ')
    for key, value in dct_.items():
        if city == value:
            print(key)
        city_amount -= 1













# rus = input('Input country with cities: ')
# lst_rus = rus.split(' ')
# fra = input('Input country with cities: ')
# lst_fra = fra.split(' ')
# ukr = input('Input country with cities: ')
# lst_ukr = ukr.split(' ')
# bel = input('Input country with cities: ')
# lst_bel = bel.split(' ')
# dct_ = dict(([(lst_rus[0], lst_rus[1:]), (lst_fra[0], lst_fra[1:3]),
#             (lst_ukr[0], lst_ukr[1:4]), (lst_bel[0], lst_bel[1:3])]))
# print(dct_)

