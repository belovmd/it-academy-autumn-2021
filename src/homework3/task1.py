"""
FizzBuzz
Напишите программу, которая печатает цифры от 1 до 100,
но вместо чисел, кратных 3 пишет Fizz, вместо чисел кратный 5
пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
"""

for num in range(1, 101):
    if not num % 3 and not num % 5:
        print('FizzBuzz')
    elif not num % 5:
        print('Buzz')
    elif not num % 3:
        print('Fizz')
    else:
        print(num)
