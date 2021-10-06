"""
5. Языки
Каждый из N школьников некоторой школы знает Mi языков. Определите,
какие языки знают все школьники и языки, которые знает хотя бы один из школьников.

Входные данные
Первая строка входных данных содержит количество школьников N. Далее идет N чисел Mi,
после каждого из чисел идет Mi строк, содержащих названия языков, которые знает i-й школьник.

Пример входных данных:
3          # N количество школьников
2          # M1 количество языков первого школьника
Russian    # языки первого школьника
English
3          # M2 количество языков второго школьника
Russian
Belarusian
English
3
Russian
Italian
French

Выходные данные
В первой строке выведите количество языков, которые знают все школьники.
Начиная со второй строки - список таких языков. Затем - количество языков,
которые знает хотя бы один школьник, на следующих строках - список таких языков.

Задачу поместите в файл task5.py в папке src/homework4.
"""

pupils_num = int(input('N: '))

languages = []
for i in range(pupils_num):
    lang_num = int(input('M: '))
    lst = []
    for j in range(lang_num):
        lst.append(input())
    languages.append(set(lst))

every_know = languages[0]
for i in range(1, pupils_num):
    every_know &= languages[i]

print()
print('Количество языков, которые знают все школьники:', len(every_know))
for el in every_know:
    print(el, end=' ')
print()

somebody_know = languages[0]
for i in range(1, pupils_num):
    somebody_know |= languages[i]

print()
print('Кол-во языков, которые значет хотя бы один школьник:', len(somebody_know))
for el in somebody_know:
    print(el, end=' ')
print()
