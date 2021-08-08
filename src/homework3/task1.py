''' Напишите программу, которая печатает цифры от 1 до 100,
но вместо чисел, кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz,
а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
'''

vivod = []
for element in range(1, 101):
    if not element % 15:
        vivod.append('FizzBuzz')
    elif not element % 3:
        vivod.append('Fizz')
    elif not element % 5:
        vivod.append('Buzz')
    else:
        vivod.append(element)
print(vivod)
