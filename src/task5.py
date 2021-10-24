# Языки
# Каждый из N школьников некоторой школы знает Mi языков.
# Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
# Входные данные
# Первая строка входных данных содержит количество школьников N.
# Далее идет N чисел Mi, после каждого из чисел идет Mi строк, содержащих названия языков,
# которые знает i-й школьник.
# Пример входных данных:
# 	3          # N количество школьников
# 2          # M1 количество языков первого школьника
# Russian    # языки первого школьника
# English
# 3          # M2 количество языков второго школьника
# Russian
# Belarusian
# English
# 3
# Russian
# Italian
# French
#
# Выходные данные
# В первой строке выведите количество языков, которые знают все школьники.
# Начиная со второй строки - список таких языков.
# Затем - количество языков, которые знает хотя бы один школьник, на следующих строках
# - список таких языков.
students = int(input('Введите количество школьников:'))
students_languages_list = []
for i in range(1, students + 1):
    num = int(input('Введите количество языков школьника: '))
    student = {input('Ведите языки, которые знает школьник: ') for element1 in range(num)}
    students_languages_list.append(student)
    print()

all = set(students_languages_list[0])
one = set(students_languages_list[0])

for language in students_languages_list:
    all = all & language
    one = one | language

print("Количество языков, которые знают все школьники: ", len(all))
for language in all:
    print(language)

print("Количество языков, которые знает хотя бы один школьник: ", len(one))
for language in one:
    print(language)

only_one = one
for i in range(0, students - 1):
    if i == students:
        break
    only_one -= students_languages_list[i] & students_languages_list[i + 1]

print("Количество языков, которые знает только один школьник: ", len(only_one))
for language in only_one:
    print(language)
