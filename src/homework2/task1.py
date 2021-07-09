rubles = int(input('Введите сумму, рублей \n'))
coins = int(input('Введите сумму, копеек \n'))
quantity = int(input('Введите количество товаров \n'))

price = ((rubles * 100) + coins) * quantity
o_r = price // 100
o_c = price % 100

if o_r != 0:
    if o_r % 10 == 1:
        if o_c % 10 == 1:
            print('Общая цена', o_r, 'рубль', o_c, 'копейка')
        elif o_c % 10 == 0 or o_c % 10 == 5 or o_c % 10 == 6 or o_c % 10 == 7 or o_c % 10 == 8 or o_c % 10 == 9:
            print('Общая цена', o_r, 'рубль', o_c, 'копеек')
        elif o_c % 10 == 2 or o_c % 10 == 3 or o_c % 10 == 4:
            print('Общая цена', o_r, 'рубль', o_c, 'копейки')
    elif o_r % 10 == 2 or o_r % 10 == 3 or o_r % 10 == 4:
        if o_c % 10 == 1:
            print('Общая цена', o_r, 'рубля', o_c, 'копейка')
        elif o_c % 10 == 0 or o_c % 10 == 5 or o_c % 10 == 6 or o_c % 10 == 7 or o_c % 10 == 8 or o_c % 10 == 9:
            print('Общая цена', o_r, 'рубля', o_c, 'копеек')
        elif o_c % 10 == 2 or o_c % 10 == 3 or o_c % 10 == 4:
            print('Общая цена', o_r, 'рубля', o_c, 'копейки')
    elif o_r % 10 == 0 or o_r % 10 == 5 or o_r % 10 == 6 or o_r % 10 == 7 or o_r % 10 == 8 or o_r % 10 == 9:
        if o_c % 10 == 1:
            print('Общая цена', o_r, 'рублей', o_c, 'копейка')
        elif o_c % 10 == 0 or o_c % 10 == 5 or o_c % 10 == 6 or o_c % 10 == 7 or o_c % 10 == 8 or o_c % 10 == 9:
            print('Общая цена', o_r, 'рублей', o_c, 'копеек')
        elif o_c % 10 == 2 or o_c % 10 == 3 or o_c % 10 == 4:
            print('Общая цена', o_r, 'рублей', o_c, 'копейки')
else:
    if o_c % 10 == 1:
        print('Общая цена', o_c, 'копейка')
    elif o_c % 10 == 0 or o_c % 10 == 5 or o_c % 10 == 6 or o_c % 10 == 7 or o_c % 10 == 8 or o_c % 10 == 9:
        print('Общая цена', o_c, 'копеек')
    elif o_c % 10 == 2 or o_c % 10 == 3 or o_c % 10 == 4:
        print('Общая цена', o_c, 'копейки')
