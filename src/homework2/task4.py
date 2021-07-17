sentence = input('Введите предложение. \n')

lower_let, upper_let = 0, 0
for element in sentence:
    if 'a' <= element <= 'z':
        lower_let += 1
    elif 'A' <= element <= 'Z':
        upper_let += 1

print('Количество строчных букв английского алфавита равно', lower_let)
print('Количество прописных букв английского алфавита равно', upper_let)
