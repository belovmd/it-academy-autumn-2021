"""
6 Слова
Во входной строке записан текст.
Словом считается последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов или символами конца строки.
Определите, сколько различных слов содержится в этом тексте.
Задачу поместите в файл task6.py в папке src/homework4.
"""

str1 = 'Скажика дядя, ведь недаром, \n дядя дядя Москва спалённая пожаром, !была французам   отдана?'

mas_from_ends = str1.split('\n')

mas_from_spaces = []

for el in mas_from_ends:
    mas_from_spaces += el.split(' ')

i = 0
while i < len(mas_from_spaces): 
    if mas_from_spaces[i] == '': 
        del mas_from_spaces[i]
    else:
        i += 1

var_words = set(mas_from_spaces)
print(len(var_words))
