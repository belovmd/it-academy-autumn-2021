sentence = input('Введите предложение. \n')

punctuation = [',', '.', ':', ';', '- ', '!', '?']

for element in punctuation:
    sentence = sentence.replace(element, '')

print(max(sentence.split(), key=len))
