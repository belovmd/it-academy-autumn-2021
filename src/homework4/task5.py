"""Языки"""

"""Каждый из N школьников некоторой школы знает Mi языков.
Определите, какие языки знают все школьники и языки,
которые знает хотя бы один из школьников.

      Входные данные
Первая строка входных данных содержит количество
школьников N. Далее идет N чисел Mi, после каждого
из чисел идет Mi строк, содержащих названия языков,
которые знает i-й школьник.

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

В первой строке выведите количество языков, 
которые знают все школьники. Начиная со второй
строки - список таких языков. Затем - количество
языков, которые знает хотя бы один школьник,
на следующих строках - список таких языков."""

number_of_students = int(input('Введите число школьников:'))
lang = []
for i in range(number_of_students):
    number_lang = int(input('Введите колличество языков школьника:'))
    sum_lang = set()
    for x in range(number_lang):
        sum_lang.add(input('Введите язык:'))
    lang.append(sum_lang)
students = set.intersection(*lang)
one_student = set.union(*lang)
print('Колличество языков, которые знают все: ', len(students), *students, sep='\n')
print('Знает хотя бы один: ', len(one_student), *one_student, sep='\n')
