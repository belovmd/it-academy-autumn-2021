rub = int(input('Введите число рублей:'))
coin = int(input('Введите число копеек:'))
count = int(input('Введите кол-во товара:'))
coinsum = coin * count
if coinsum >= 100:
    rub = rub * count + (coinsum // 100)
    coinsum = coinsum % 100
else:
    rub = rub * count
print("Сумма товаров ровна ", rub, 'рублей', coinsum, 'копеек')