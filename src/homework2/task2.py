"""Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания."""
my_str = input('Введите строку: ')
punctuation = '.,!?:;+-*)(_%"\''

for mark in punctuation:
    my_str = my_str.replace(mark, '')

words = my_str.split(' ')
longest_word = ''

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print(longest_word)

