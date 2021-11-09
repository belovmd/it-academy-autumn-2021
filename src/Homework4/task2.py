''' Города
Дан список стран и городов каждой страны. Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.

Входные данные
Программа получает на вход количество стран N. Далее идет N строк,
каждая строка начинается с названия страны, затем идут названия городов
этой страны. В следующей строке записано число M,
далее идут M запросов — названия каких-то M городов, перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны, в котором находится данный город.

Входные данные
4
Russia Moscow Petersburg Novgorod Kaluga
France Brest Paris
Ukraine Kiev Donetsk Odessa
Belarus Minsk Brest	
3
Odessa
Moscow
Brest
Выходные данные
Ukraine
Russia
France Belarus
'''

n = int(input())     
dct = {}                                 
for _ in range(n):           
    country, *cities = input().split()
    for city in cities:
        if city in dct:
            dct[city] = dct[city] + ' ' + country
            m = int(input())
            for _ in range(m):
                print(dct[input()])
        else:
            dct[city] = country            
