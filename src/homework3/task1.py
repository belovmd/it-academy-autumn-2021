"""
Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел, кратных 3 пишет Fizz,
вместо чисел кратный 5 пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
"""

for i in range(101):
    if not i % 5 and not i % 3:
        print('FizzBuzz')
    elif not i % 3:
        print('Fizz')
    elif not i % 5:
        print('Buzz')
    else:
        print(i)
