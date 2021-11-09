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
English
Russian
French
Italian
Belarusian
'''

intersection = set()
all_ = set()
dct = {}
for element in range(int(input('Количество школьников: '))):
    dct[element] = {input() for j in range(int(input('Количество языков, которые знает школьник: ')))}
intersection = set.intersection(*dct.values())
all_ = set.union(*dct.values())
print(len(intersection))      # языки, которые знают все школьники
print('\n'.join(intersection))
print(len(all_))               # языки, которые знает хотя бы один из школьников
print('\n'.join(all_))
