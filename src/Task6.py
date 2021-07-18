def palindrom():
    while True:
        number = input("Введите число")
        try:
            number = int(number)
            break
        except ValueError:
            print("Неверное число!")
            continue
    print(number)


    n = 10
    while (number // n) > 10:
        n *= 10

    factor = 1
    num = number
    number_reverse = 0
    while n >= 1:
        cipher = (num // n)
        number_reverse += cipher*factor
        num = num - cipher * n
        n = n / 10
        factor *= 10

    if number_reverse != number:
        print("Не палиндром")
    else:
        print("Палиндром")


if __name__ == '__main__':
    palindrom()