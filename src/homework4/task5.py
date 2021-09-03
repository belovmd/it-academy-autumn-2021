"""
Каждый из N школьников некоторой школы знает Mi языков.
Определите, какие языки знают все школьники и языки,
которые знает хотя бы один из школьников.

Входные данные
Первая строка входных данных содержит количество школьников N.
Далее идет N чисел Mi, после каждого из чисел идет Mi строк,
содержащих названия языков, которые знает i-й школьник.

Пример входных данных:
3
2
Russian
English
3
Russian
Belarusian
English
3
Russian
Italian
French

Выходные данные
В первой строке выведите количество языков, которые знают
все школьники. Начиная со второй строки - список таких языков.
Затем - количество языков,которые знает хотя бы один школьник,
на следующих строках - список таких языков.
"""

from functools import reduce

q_of_pupils = int(input('Введите количество школьников: '))
lst_of_lang = []
for _ in range(q_of_pupils):
    q_of_lang = int(input('Введите количество языков: '))
    set_of_lang = set()
    for _ in range(q_of_lang):
        language = input('Введите язык: ')
        set_of_lang.add(language)
    lst_of_lang.append(set_of_lang)

answer1 = reduce((lambda a, b: a & b), lst_of_lang)
print(len(answer1))
print(list(answer1))

answer2 = reduce((lambda a, b: a ^ b), lst_of_lang)
print(len(answer2))
print(list(answer2))
