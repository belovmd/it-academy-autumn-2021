rubles = int(input('Введите сумму, рублей: \n'))
coins = int(input('Введите сумму, копеек: \n'))
quantity = int(input('Введите количество товаров: \n'))

price = ((rubles*100) + coins)*quantity
rub = price // 100
con = price % 100

if rub % 10 == 1:
    if con % 10 == 1:
        print('Общая цена', rub, 'рубль', con, 'копейка')
    elif con % 10 or 5 <= con % 10 <= 9:
        print('Общая цена', rub, 'рубль', con, 'копеек')
    elif 2 <= con % 10 <= 4:
        print('Общая цена', rub, 'рубль', con, 'копейки')
elif 2 <= rub % 10 <= 4:
    if con % 10 == 1:
        print('Общая цена', rub, 'рубля', con, 'копейка')
    elif con % 10 or 5 <= con % 10 <= 9:
        print('Общая цена', rub, 'рубля', con, 'копеек')
    elif 2 <= con % 10 <= 4:
        print('Общая цена', rub, 'рубля', con, 'копейки')
elif rub % 10 or 5 <= rub % 10 <= 9:
    if con % 10 == 1:
        print('Общая цена', rub, 'рублей', con, 'копейка')
    elif con % 10 or 5 <= con % 10 <= 9:
        print('Общая цена', rub, 'рублей', con, 'копеек')
    elif 2 <= con % 10 <= 4:
        print('Общая цена', rub, 'рублей', con, 'копейки')
elif not rub:
    if con % 10 == 1:
        print('Общая цена', con, 'копейка')
    elif con % 10 or 5 <= con % 10 <= 9:
        print('Общая цена', con, 'копеек')
    elif 2 <= con % 10 <= 4:
        print('Общая цена', con, 'копейки')
