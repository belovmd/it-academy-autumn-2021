"""
2. Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания.
Подсказки:
-	my_string.split([chars]) возвращает список строк.
-	len(list) - количество элементов в списке
"""

my_string = input('Введите предложение: ')

largword = ''
punctuation_marks = ',.!:-?№/'

for mark in punctuation_marks:
    my_string = my_string.replace(mark,'')

my_string = my_string.split(' ')

for word in my_string:
    if len(word) > len(largword):
        largword = word

print(largword)