#Функция которая рассчитывает стоимость товара


def cost():
    while True:
        l = input("Введите количество товаров:")
        try:
            l = int(l)
        except:
            print("Вы должны ввести целое число!")
            continue
        m = input("Введите рубли стоимости:")
        try:
            m = int(m)
        except:
            print("Вы должны ввести целое число!")
            continue
        n = input("Введите копейки стоимости:")
        try:
            n = int(n)
        except:
            print("Вы должны ввести целое число!")
            continue
        break

    cost_rubles = l*m + l*n//100
    cost_centime = (l*n)%100
    sum = f"Общая стоимость: {cost_rubles} рублей {cost_centime} копеек"
    print(sum)



if __name__ == '__main__':
    cost()
