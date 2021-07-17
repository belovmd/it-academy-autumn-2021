number_inp = int(input('Введите число: '))
number = number_inp

pal = 0
while number > 0:
    new_number = number % 10
    pal = pal*10 + new_number
    number = number // 10

if number_inp != pal:
    print('Это не палиндром')
else:
    print('Это палиндром')
