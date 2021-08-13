"""
Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,
кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz, а вместо чисел
одновременно кратных и 3 и 5 - FizzBuzz.
"""


for number in range(1, 101):
    if not number % 3 and not number % 5:
        number = 'FizzBuzz'
    elif not number % 3:
        number = 'Fizz'
    elif not number % 5:
        number = 'Buzz'
    print(number)
