import math


# task1
def total_sum():
    m = int(input('Введите цену, руб.:'))
    n = int(input('Введите цену, коп.:'))
    s = int(input('Введите колиечство товара:'))
    total = s * (m + (n / 100)) * 100
    rub = int(total // 100)
    cent = int(total % (total // 100 * 100))
    template = "Общая стоимость: {rub} руб. {cent} коп."
    print(template.format(rub=rub, cent=cent))
    return print()


# task2
def longest_word():
    my_string = input('Input the string: ')
    template = "The longest word is : {longest_word}"
    punctuation_marks = r'\'"#!$%&()*+,-./:;<=>?@[\]^_{|}~'
    for mark in punctuation_marks:
        my_string = my_string.replace(mark, '')
        clear_string = my_string.split(' ')
        longest_word = ''
        for word in clear_string:
            if len(word) > len(longest_word):
                longest_word = word
    print(template.format(longest_word=longest_word))
    return print()


# task3
def unique_symbols():
    my_string = input('Input the string: ')
    my_string = my_string.replace(' ', '')
    new_string = my_string[0]
    template = "The string of unique symbols is : {new_string}"
    for i in range(len(my_string)):
        if my_string[i] not in new_string:
            new_string += my_string[i]
        else:
            new_string = new_string
    print(template.format(new_string=new_string))
    return print()


# task4
def quantity_upper_lower_case_letters():
    my_string = input('Input the string: ')
    template = "Number of uppercase latin letters : {upper_case} " \
               "\nNumber of lowercase latin letters : {lower_case}"
    upper_case = 0
    lower_case = 0
    for symbol in my_string:
        if str.isupper(symbol) and 'A' <= symbol <= 'Z':
            upper_case += 1
        if str.islower(symbol) and 'a' <= symbol <= 'z':
            lower_case += 1
    print(template.format(upper_case=upper_case, lower_case=lower_case))
    return print()


# task5
def fibonacci_numbers():
    n = int(input('Введите число n: '))
    template = "Число Фибоначчи = {fib}"
    a = 0
    b = 1
    if n < 0:
        print('Negative')
    elif n <= 1:
        b = n
        print(template.format(fib=b))
    else:
        a, b = b, a + b
        for _ in range(n - 2):
            a, b = b, a + b
    print(template.format(fib=b))
    return print()


# task6
def palindrome():
    x = int(input('Введите число больше 0: '))
    input_dig = x
    reverse_dig = 0
    while x:
        last_dig = x % 10
        reverse_dig = reverse_dig * 10 + last_dig
        x = x // 10
    if input_dig != reverse_dig:
        print('Не палиндром')
    else:
        print('Палиндром')
    return print()


# task7
def triangle_square():
    a = float(input('Введите 1-ю сторону треугольника: '))
    b = float(input('Введите 1-ю сторону треугольника: '))
    c = float(input('Введите 1-ю сторону треугольника: '))
    if a + b >= c and b + c >= a and a + c >= b:
        p = (a + b + c) / 2
        square = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print('Площадь треугольника', square)
    else:
        print('Введены неверные данные. Фигура не является треугольником')
    return print()
