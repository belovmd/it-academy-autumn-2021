# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.
# Входные данные
# Программа получает на вход количество стран N.
# Далее идет N строк, каждая строка начинается с названия страны, 
# затем идут названия городов этой страны.
# В следующей строке записано число M,
# далее идут M запросов — названия каких-то M городов, перечисленных выше.

n = int(input('How many countries would you like to input?\n'))
dct = {}
for number in range(n):
    cities = [str(x) for x in input().split()]
    for element in cities:
        dct.setdefault(cities[0], []).append(element)
n_choice = int(input('How many cities would you like to check?\n'))
for times in range(n_choice):
    choice = str(input())
    for city in dct.values():
        if choice in city:
            print(city[0])
