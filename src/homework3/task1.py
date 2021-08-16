'''FizzBuzz
Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,
кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz,
а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz'''

list = []
for i in range(1, 101):
    if (i % 15) == 0:
        list.append("FizzBuzz")
    elif i % 3 == 0:
        list.append('Fizz')
    elif i % 5 == 0:
        list.append('Buzz')
    else:
        list.append(i)
print(list)
