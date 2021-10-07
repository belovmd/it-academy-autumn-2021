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
n = int(input('Введите количество школьников:'))
students_languages_list = []
for _ in range(1, n + 1):
    m = int(input('Введите количество языков школьника: '))
    student = {input('Ведите языки, которые знает школьник: ') for element1 in range(m)}
    students_languages_list.append(student)
    print()

all_ = set(students_languages_list[0])
one_ = set(students_languages_list[0])

for language in students_languages_list:
    all_ = all_ & language
    one_ = one_ | language

print("Количество языков, которые знают все школьники: ", len(all_))
for language in all_:
    print(language)

print("Количество языков, которые знает хотя бы один школьник: ", len(one_))
for language in one_:
    print(language)

just_one = one_
for i in range(0, n - 1):
    if i == n:
        break
    just_one -= students_languages_list[i] & students_languages_list[i + 1]

print("Count languages just one student knows: ", len(just_one))
for language in just_one:
    print(language)
