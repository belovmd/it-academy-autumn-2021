# Пары элементов
# Дан список чисел. Посчитайте, сколько в нем пар элементов,
# равных друг другу. Считается, что любые два элемента,
# равные друг другу образуют одну пару, которую необходимо посчитать.
# Входные данные - строка из чисел, разделенная пробелами.
# Выходные данные - количество пар.
# Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар

lst = [int(element) for element in input('The list of diigits: ').split()]
pair_count = 0
for item in range(len(lst)):
    for element in range(item + 1, len(lst)):
        if lst[item] == lst[element]:
            pair_count += 1
print('The count of pair elements is', pair_count)
