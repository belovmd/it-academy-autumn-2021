"""HW 3.1. FizzBuzz
Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел, кратных 3 пишет Fizz,
вместо чисел кратных 5 пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz"""


def fizzbuzz():
    lst = []
    for x in range(1, 101):
        if not x % 15:
            lst.append('FizzBuzz')
        elif not x % 3:
            lst.append('Fizz')
        elif not x % 5:
            lst.append('Buzz')
        else:
            lst.append(x)
    return lst


"""HW 3.4. Пары элементов
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается,
что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар"""


def pairs():
    input_lst = input('Введите числа, разделенные пробелами: ').split()
    count_elements = {element: input_lst.count(element) for element in input_lst}
    one_pair_sum = [value * (value - 1) // 2 for value in count_elements.values()]
    return one_pair_sum


"""HW 3.5. Уникальные элементы в списке
Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке."""


def unique_elements():
    lst = list(input('Введите список: '))
    lst_output = [element for element in lst if lst.count(element) == 1]
    return lst_output
