""" Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
    Например, если было введено "abc cde def", то должно быть выведено "abcdef".
    Подсказка: оператор in проверяет, входит ли подстрока в строку или нет.
"""

sentence = input('Введите предложение. \n')

sentence = sentence.replace(' ', '')

letters = []
for element in sentence:
    if element not in letters:
        letters.append(element)

print(''.join(letters))
