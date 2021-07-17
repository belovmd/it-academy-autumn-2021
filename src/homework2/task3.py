sentence = input('Введите предложение. \n')

sentence = sentence.replace(' ', '')

letters = []
for element in sentence:
    if element not in letters:
        letters.append(element)

print(''.join(letters))
