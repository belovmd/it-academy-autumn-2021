"""
Каждый из N школьников некоторой школы знает Mi языков.
Определите, какие языки знают все школьники и языки,
которые знает хотя бы один из школьников.
Входные данные
Первая строка входных данных содержит количество школьников N.
Далее идет N чисел Mi, после каждого из чисел идет Mi строк,
содержащих названия языков, которые знает i-й школьник.
"""

n = int(input('Введите количество школьников '))

dct = {}

for i in range(1, n + 1):
    lengs = int(input('сколько языков знает ученик '))
    lst_ = []
    for b in range(1, lengs + 1):
        lst_.append(input())
        dct[i] = lst_

uniq = set(dct[1])
all_know = set(dct[1])

for i in range(1, len(dct) + 1):
    all_know = all_know & set(dct[i])
    uniq = uniq | set(dct[i])

uniq = uniq - all_know

print('Все знают', len(all_know))
for leng in all_know:
    print(leng)

print('Хотя бы один ученик знает', len(uniq))
for leng in uniq:
    print(leng)
