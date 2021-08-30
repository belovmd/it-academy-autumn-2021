"""
Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел, кратных 3 пишет Fizz,
вместо чисел кратный 5 пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
"""
fizz = 3
buzz = 5

for i in range(1, 101):
    if not i % buzz and not i % fizz:
        print('FizzBuzz')
    elif not i % fizz:
        print('Fizz')
    elif not i % buzz:
        print('Buzz')
    else:
        print(i)
