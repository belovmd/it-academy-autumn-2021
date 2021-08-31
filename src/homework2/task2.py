# Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания
# Подсказки:
# my_string.split([chars]) возвращает список строк.
# len(list) - количество элементов в списке
import string
result = string.punctuation
sentence = str(input())
for letter in sentence:
    if letter in result:
        sentence = sentence.replace(letter, '')
sentence = sentence.split()
print('The longest word in the sentence is: ', max(sentence, key=len))
