'''
hw4: 1
Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,
кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz, а вместо чисел
одновременно кратных и 3 и 5 - FizzBuzz.
'''


def fizzbuzz():
    lst = []
    for num in range(100):
        if not num % 15:
            lst.append('FizzBuzz')
        elif not num % 3:
            lst.append('Fizz')
        elif not num % 5:
            lst.append('Buzz')
        else:
            lst.append(num)
    print(lst)


'''
hw3: 1
Создайте словарь с помощью генератора словарей, так чтобы его ключами были числа от 1 до 20,
а значениями кубы этих чисел.
'''


def cubes():
    dct = {key: key ** 3 for key in range(1, 21)}
    print(dct)


'''
hw3: 4
Пары элементов
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару, которую
необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар.
'''


def pairs():
    lst = [int(s) for s in input('Введите числа через пробел: ').split()]
    dct = {num: lst.count(num) for num in lst}
    couples = [sum(range(value)) for value in dct.values()]
    print(sum(couples))
