'''Посчитать количество строчных (маленьких) и прописных (больших) букв
    в введенной строке.
    Учитывать только английские буквы.
'''

str_ = input('Введите стоку: ')
count_mal = 0
count_bol = 0
for element in range(len(str_)):
    # проверяем на вхождение в диапазон прописных латинских букв A-Z
    if 65 < ord(str_[element]) < 90:
        count_bol += 1
    else:
        # a-z
        if 97 < ord(str_[element]) < 122:
            count_mal += 1
print('Строчных букв:', count_bol, 'прописных:', count_mal)
