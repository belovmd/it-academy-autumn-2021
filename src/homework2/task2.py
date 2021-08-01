'''Найти самое длинное слово в введенном предложении.
   Учтите что в предложении есть знаки препинания.
'''

predl = input('Введите предложение: ')
i = predl.split(' ')
predl = []
for element in i:
    element = element.strip('.,:;!?)')
    predl.append(element)
print('Самое длинное слово: ', max(predl, key=len))
