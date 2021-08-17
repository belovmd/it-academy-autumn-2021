'''
Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
Подсказки:
my_string.split([chars]) возвращает список строк.
len(list) - количество элементов в списке.
'''


sent = input('Введите предложение: ')
punctuation_marks = '.,-;:?!"@№#$%^&*'

for mark in punctuation_marks:
    sent = sent.replace(mark, '')

words = sent.split(' ')
longest_word = max(words, key=len)
print('Самое длинное слово в предложении —', longest_word.lower())
