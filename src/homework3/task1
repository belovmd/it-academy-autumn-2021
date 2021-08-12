# Напишите программу, которая печатает цифры от 1 до 100,
# но вместо чисел, кратных 3 пишет Fizz,
# вместо чисел кратный 5 пишет Buzz,
# а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz

digits = [i for i in range(1, 101)]
new_list = []
for item in digits:  # multiple of 3
    if item % 3:
        new_list.append('Fizz')
    if item % 5:
        new_list.append('Buzz')
    if (item % 3) and (item % 5):
        new_list.append('FizzBuzz')
    else:
        new_list.append(item)
print(new_list)
