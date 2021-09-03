"""FizzBuzz
Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел, кратных 3 пишет Fizz,
вместо чисел кратный 5 пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
"""


def crazy_function():
    list_ = []
    for i in range(1, 101):
        if not i % 3 and not i % 5:
            list_.append('FizzBuzz')
        elif not i % 5:
            list_.append('Buzz')
        elif not i % 3:
            list_.append('Fizz')
        else:
            list_.append(i)
    return list_


if __name__ == '__main__':
    print(crazy_function())
