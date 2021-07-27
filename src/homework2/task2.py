"""
2. Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания.
Подсказки:
-	my_string.split([chars]) возвращает список строк.
-	len(list) - количество элементов в списке
"""

my_string = input('Введите предложение: ')

larg_word = ''
punctuation_marks = ',.!:-?№/'

for mark in punctuation_marks:
    my_string = my_string.replace(mark, '')

my_string = my_string.split(' ')

for word in my_string:
    if len(word) > len(larg_word):
        larg_word = word

print(larg_word)
