# Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def", то должно быть выведено "abcdef".

text = input('Please, input the text: ')
text_list = ''
for i in text:
    if i not in text_list and i != ' ':
        text_list += i
print(text_list)
