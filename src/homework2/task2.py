"""Найти самое длинное слово в введенном предложении.
   Учтите что в предложении есть знаки препинания.
  Подсказки:
  -	my_string.split([chars]) возвращает список строк.
  -	len(list) - количество элементов в списке
"""


s = str(input('Введите предложение: '))

mark_list = '.,!?:;()-+"%$@[]{}=&*#'
for mark in mark_list:
    s = s.replace(mark, '')

mark_list = "'"
for mark in mark_list:
    s = s.replace(mark, '')

list_words = s.split()

max_len = 0
max_word = ''

for word in list_words:
    len_word = len(word)
    if len_word > max_len:
        max_len = len_word
        max_word = word

print('Самое длинное слово: \"', max_word, '\"')
