"""
Библиотека с функциями для task1 из HomeWork5
# hw4task1  +
# hw3task3  +
# hw3task4  +
# hw3task5  +
# hw3task6  +
"""


def hw4task1():
    print()
    print('Функция hw4task1()')

    a = {el: el ** 3 for el in range(1, 21)}
    for el in a:
        print(el, ':', a[el])


"""Tuple practice
Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
Создайте кортеж из одного элемента, чтобы при итерировании по этому элементу
последовательно выводились значения 1, 2, 3. Убедитесь что len() исходного кортежа возвращает 1.
"""


def hw3task3():
    print()
    print('Функция hw3task3()')    
    # Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
    spis = ['a', 'b', 'c']
    kort = tuple(spis)
    print(kort)
    # Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
    kort2 = ('a', 'b', 'c')
    spis2 = list(kort2)
    print(spis2)

    # Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
    a, b, c = 'a', 2, 'python'
    print(a, b, c)

    # Создайте кортеж из одного элемента, чтобы при итерировании по этому элементу
    kort3 = ((1, 2, 3),)
    for el in kort3[0]:
        print(el)
    print('len() kort3:', len(kort3))


"""
Пары элементов
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
"""


def hw3task4():
    print()
    print('Функция hw3task4()')

    input_str = '1 23 34 0 0 1 0'
    input_list = input_str.split()
    print(input_list)

    num_list = [int(i) for i in input_list]
    print(num_list)

    par_count = 0
    for i in range(len(num_list) - 1):
        for j in range(i + 1, len(num_list)):
            if num_list[i] == num_list[j]:
                par_count += 1

    print('Number of pairs:', par_count)


"""
5 Уникальные элементы в списке
Дан список. Выведите те его элементы, которые встречаются в списке только один раз. 
Элементы нужно выводить в том порядке, в котором они встречаются в списке.
Задачу поместите в файл task5.py в папке src/homework3.
"""


def hw3task5():
    print()
    print('Функция hw3task5()')

    input_list = [0, 2, 5, 7, 45, 23, 0, 7, 8, 100, 34, 36, 2]
    print(input_list)

    for i in range(len(input_list)):
        for j in range(len(input_list)):
            if not i == j:  # исключение проверки самого себя
                if input_list[i] == input_list[j]:
                    break
                elif j == len(input_list) - 1:
                    print(input_list[i], end=' ')
    print()


"""
6 Упорядоченный список.
Дан список целых чисел. Требуется переместить все ненулевые элементы в левую часть списка,
не меняя их порядок, а все нули - в правую часть. Порядок ненулевых элементов изменять нельзя,
дополнительный список использовать нельзя, задачу нужно выполнить за один проход по списку.
Распечатайте полученный список.
Задачу поместите в файл task6.py в папке src/homework3.
"""


def hw3task6():
    print()
    print('Функция hw3task6()')

    a = [0, 2, 0, 3, 7, 2, 0, 4, 0, 12, 34, 87, 17, 0, 100, -3, -8, 0, 22]
    print(a)
    b = 0
    for i in range(len(a) - 1):
        if not a[i]:
            for j in range(i + 1, len(a)):
                if a[j]:
                    b = a[i]
                    a[i] = a[j]
                    a[j] = b
                    break
    print(a)
