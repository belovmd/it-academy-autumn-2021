"""
Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
"""

str_ = input('Print your sentence: ')
punctuation_marks = '.,-;:?!'
for mark in punctuation_marks:
    str_ = str_.replace(mark, '')
words = str_.split(' ')
longest_word = ''
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print(longest_word)
