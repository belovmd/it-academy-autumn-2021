'''Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания
Подсказки:
my_string.split([chars]) возвращает список строк.
len(list) - количество элементов в списке'''

string = input("write sentences->")
punctuation = '.,!?:;+-*)(_%"\''
for mark in punctuation:
    string = string.replace(mark, '')
longest_word = " "
for word in string.split():
    if len(word) > len(longest_word):
        longest_word = word
print(longest_word)
