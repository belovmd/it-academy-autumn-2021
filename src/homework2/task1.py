''' Напишите программу, которая считает общую цену.
   Вводится M рублей и N копеек цена, а также количество S товара.
   Посчитайте общую цену в рублях и копейках за L товаров.
   Пример:
   Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
   Output: Общая цена 9 рублей 60 копеек
'''


M = int(input('Введите стоимость, руб.: '))
N = int(input('Введите стоимость, коп.: '))
S = int(input('Введите количество товара: '))
stoim = S * (M + N / 100)
print("Общая цена: ",  int(stoim // 1), 'руб.', int(stoim % 1 * 100), 'коп.')
