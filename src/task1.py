'''
Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,
кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz, а вместо чисел
одновременно кратных и 3 и 5 - FizzBuzz.
'''


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
