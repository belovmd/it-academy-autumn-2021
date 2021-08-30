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
import re
# str_ = 'a       b b c'
# lst_ = []
# str_ = str_.replace(' ', '')
# for i in str_:
#     lst_.append(i)
# print(lst_)

str_ = 'aaa5 55      b b c \n'
lst_ = re.findall(r'\S+', str_)
print(lst_, len(lst_))
