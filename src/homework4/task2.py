# Города
# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.
# Входные данные
# Программа получает на вход количество стран N.
# Далее идет N строк, каждая строка начинается с названия страны,
# затем идут названия городов этой страны. В следующей строке записано число M,
# далее идут M запросов — названия каких-то M городов, перечисленных выше.
# Выходные данные
# Для каждого из запроса выведите название страны, в котором находится данный город.
# Примеры
#
# Входные данные
# 4
# Russia Moscow Petersburg Novgorod Kaluga
# France Brest Paris
# Ukraine Kiev Donetsk Odessa
# Belarus Minsk Brest
#
#
# 3
# Odessa
# Moscow
# Novgorod
#
# Выходные данные
# Ukraine
# Russia
# Russia
n = int(input('Введите количество стран: '))
country_city_dict = {}
for _ in range(n):
    a, *b = input('Введите название страны и ее города: ').split()
    country_city_dict[a] = b

m = int(input('Введите количество городов: '))
city_list = []
for _ in range(m):
    search_city = (input('Введите название города: '))
    city_list.append(search_city)
for city in city_list:
    countries = []
    for key, value in country_city_dict.items():
        if city in value:
            countries.append(key)
    print(', '.join(countries))
