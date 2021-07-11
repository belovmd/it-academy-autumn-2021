def count():
    a = "Введите количество товаров:"
    b = "Введите рубли:"
    c = "Введите копейки:"
    proposals = [a, b, c]
    data = {'quantity': 0,
            'rubles': 0,
            'centimes': 0}

    i = 0
    keylist = list(data)
    for proposal in proposals:
        while True:
            number = input(proposal)
            try:
                number = int(number)
                data[keylist[i]] = number
                i = i + 1
                break
            except:
                print("Введите целое число!")
                continue

    print(data)

    summa = data['quantity'] * data['rubles'] + \
            (data['quantity'] * data['centimes']) // 100 + \
            (data['quantity'] * data['centimes'] % 100) / 100
    print("Цена партии товара %.f рублей" % summa)


if __name__ == '__main__':
    while True:
        count()
        answer = input("Новый расчет? Д/Н")
        if answer.lower() == 'н':
            break
        else:
            continue
