'''Посчитать количество строчных (маленьких) и прописных (больших) букв
    в введенной строке.
    Учитывать только английские буквы.
'''

str_ = input('Введите стоку: ')
low_letters = [i for i in str_ if 'a' <= i <= 'z']
upper_letters = [i for i in str_ if 'A' <= i <= 'Z']
print('Количество строчных букв:', len(low_letters), '\nпрописных букв:', len(upper_letters))
