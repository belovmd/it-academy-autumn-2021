"""Пары элементов
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""

count = 0
lst_ = []
str_ = (input('Input your sting of numbers: '))
str_ = str_.strip()
str_ = str_.split(' ')
for i in str_:
    lst_.append(int(i))
for el in lst_:
    if lst_[el] == lst_[el + 1]:
        count += 1
print(count)
