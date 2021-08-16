'''Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef"
'''

print('Введите некоторую строку')
str1 = input()
str2 = ''
for element in str1:
    if element not in str2 and element != ' ':
        str2 += element
print('Новая строка: ', str2)
