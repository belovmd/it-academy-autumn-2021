'''Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар'''

str = '1 1 2 4 1 5'
lst1 = str.split()
b = 0
for i in range(len(lst1)):             # или так__a = input().split()
    for j in range(i + 1, len(lst1)):  # _________print(sum(a.count(x) - 1 for x in a) // 2)
        if lst1[i] == lst1[j]:
            b += 1
print(b)
