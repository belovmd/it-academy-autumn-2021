'''Найти самое длинное слово в введенном предложении.
   Учтите что в предложении есть знаки препинания.
'''

predl = input('Введите предложение: ')
predl_new = []
for element in predl.split(' '):
    element = element.strip('.,:;!?-{}()[]\"\'')
    predl_new.append(element)
print('Самое длинное слово: ', max(predl_new, key=len))
