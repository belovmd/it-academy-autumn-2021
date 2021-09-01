''' Языки
Каждый из N школьников некоторой школы знает Mi языков.
Определите, какие языки знают все школьники
и языки, которые знает хотя бы один из школьников.

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
1
Russian
5
Belarusian
English
French
Italian
Russian
'''

intersection = set()
all_ = set()
n = int(input())
for element in range(n):
    m = int(input())
    a = {input() for j in range(m)}
    all_ |= a
    if element == 1:
        intersection |= a
    else:
        intersection &= a
print(len(intersection), '\n', ' '.join(intersection))
print(len(all_), '\n', ' '.join(all_))
