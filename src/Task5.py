def fibonachi():
    while True:
        n = input("Введите n:")
        try:
            n = int(n)
            break
        except ValueError:
            print("Нужно ввести целое число!")
            continue

    data = [0, 1]
    i = 0
    while i < n - 2:
        data.append(data[i] + data[i + 1])
        i += 1
    print("Элемент под номером %i числовой последовательносии Фибоначи: %i" % (n, data[-1]))


if __name__ == '__main__':
    while True:
        fibonachi()
        answer = input("Press 'Q' to quit")
        if answer.lower() == 'q':
            break
        else:
            continue
