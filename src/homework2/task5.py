num = int(input('Введите порядковый номер числа ряда Фибоначчи: '))
num0 = 0
num1 = 1
num = num - 1
while num > 0:
    num2 = num1
    num1 = num0 + num1
    num0 = num2
    num = num - 1
print('Это число - ', num0)






