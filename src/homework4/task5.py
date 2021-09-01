"""Каждый из N школьников некоторой школы знает Mi языков.
Определите, какие языки знают все школьники и языки,
которые знает хотя бы один из школьников.
"""
students = int(input('Введите колличество школьников: '))
language = []
for i in range(students):
    lancost = int(input('Введите колличество языков школьника: '))
    sum_lan = set()
    for j in range(lancost):
        sum_lan.add(input('Введите язык: '))
    language.append(sum_lan)
all_students = set.intersection(*language)
some_students = set.union(*language)
print('Колличество языков, которые знают все: ', len(all_students), *all_students, sep='\n')
print('Знает хотя бы один: ', len(some_students), *some_students, sep='\n')
