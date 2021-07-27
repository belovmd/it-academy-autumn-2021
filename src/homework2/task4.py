"""
4. Посчитать количество строчных (маленьких) и прописных (больших) букв в
введенной строке. Учитывать только английские буквы.
"""

import string

only_eng = ''
low_eng = ''
up_eng = ''

inp_str = input('Введите строку: ')

for i in inp_str:
    if i in string.ascii_letters:
        only_eng += i

for i in only_eng:
    if i.islower():
        low_eng += i
    else:
        up_eng += i

print('больших букв -', len(up_eng))
print('маленьких букв -', len(low_eng))
