""" Найти самое длинное слово в введенном предложении.
    В случае если их несколько, самое левое в строке. Учтите,
    что в предложении есть знаки препинания.
"""

sentence = input('Введите предложение. \n')

punctuation = [',', '.', ':', ';', '- ', '!', '?']

for element in punctuation:
    sentence = sentence.replace(element, '')

print(max(sentence.split(), key=len))
