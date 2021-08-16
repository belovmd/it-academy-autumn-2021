'''FizzBuzz
Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,
кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz,
а вместо чисел одновременно кратных 3 и 5 - FizzBuzz'''

list = []
for i in range(1, 101):
    if not (i % 15):
        list.append("FizzBuzz")
    elif not i % 3:
        list.append('Fizz')
    elif not i % 5:
        list.append('Buzz')
    else:
        list.append(i)
print(list)
