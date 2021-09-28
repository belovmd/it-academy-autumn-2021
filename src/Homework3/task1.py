"""1. FizzBuzz
Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел, кратных 3 пишет Fizz,
вместо чисел кратных 5 пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz"""
for x in range(1, 101):
    if not x % 15:
        print('FizzBuzz')
    elif not x % 3:
        print('Fizz')
    elif not x % 5:
        print('Buzz')
    else:
        print(x)
