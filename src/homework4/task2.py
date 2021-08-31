"""
2 Города
Дан список стран и городов каждой страны. Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.

Входные данные
Программа получает на вход количество стран N. Далее идет N строк,
каждая строка начинается с названия страны, затем идут названия городов
этой страны. В следующей строке записано число M,
далее идут M запросов — названия каких-то M городов, перечисленных выше.

Выходные данные
Для каждого из запроса выведите название страны, в котором находится
данный город.

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

Задачу поместите в файл task2.py в папке src/homework4.
"""

N = int(input('Задайте кол-во строк N (кол-во вводимых стран с городами): '))

print('Введите страну и города (через пробел): ')
inp_data = []
for i in range(N):
    print(i + 1, ':', end=' ')
    str_ = input()
    inp_data.append(str_.split())

print()
M = int(input('Задайте кол-во городов M: '))
print('Введите города: ')
towns = []
for i in range(M):
    print(i + 1, ':', end=' ')
    towns.append(input())

towns_in_country = \
    {inp_data[i][0]: [inp_data[i][j] for j in range(1, len(inp_data[i]))] for i in range(N)}

print()
num_countries = 0
for town in towns:
    num_countries = 0
    for key, value in towns_in_country.items():
        if town in value:
            num_countries += 1
            print(key, end=' ')  # страны с одинаковым городом выводим в одной строчке
    if not num_countries:
        print('--')  # если в словаре нет страны для этого города (с переходом на след строку)
    else:
        print('')  # если нашли хотя бы одну страну, то перейдём на след строку (завершим текущую)
