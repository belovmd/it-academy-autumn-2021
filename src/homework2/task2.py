"""Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания.
  Подсказки:
  -	my_string.split([chars]) возвращает список строк.
  -	len(list) - количество элементов в списке
"""


s = str(input('Введите предложение: '))
# s = 'Ехали бояре, кошку потеряли. Кошка сдохла, хвост облез: кто промолвит, тот и съест!'

mark_list = '.,!?:;()'
for mark in mark_list:
    s = s.replace(mark, '')

list_words = s.split()

max_len = 0  # max длина слова
max_word = ''  # слово максимальной длины

for word in list_words:
    len_word = len(word)
    if len_word > max_len:
        max_len = len_word
        max_word = word

print('Самое длинное слово: \"', max_word, '\"')
# print('Его длина равна', max_len)
