'''Найти самое длинное слово в введенном предложении. Учтите что в предложении
есть знаки препинания.
Подсказки:
my_string.split([chars]) возвращает список строк.
len(list) - количество элементов в списке
'''

print('Введите предложение')
my_string = input()
long = ''
punkt_marks = '.,!?;:-'
for _ in punkt_marks:
    my_string = my_string.replace(_, '')
my_string = my_string.split(' ')
for list in my_string:
    if len(list) > len(long):
        long = list
print(long)
