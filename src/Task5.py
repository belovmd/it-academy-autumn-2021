# Выведите n-ое число Фибоначчи, используя только временные переменные,
# циклические операторы и условные операторы. n - вводится


def fibonachi():
    # проверка, что пользователь ввел int, если не ввод не int предлагается повторный int
    while True:
        n = input("Введите n:")
        try:
            n = int(n)
            break
        except ValueError:
            print("Нужно ввести целое число!")
            continue

    # list который задает последовательность Фибоначи длиной заданной пользователем
    data = [0, 1]
    i = 0
    while i < n - 2:
        data.append(data[i] + data[i + 1])
        i += 1
    print("Элемент под номером %i числовой последовательносии Фибоначи: %i" % (n, data[-1]))


# Пользоваетль может бесконечно использовать функцию до тех пор пока сам не выйдет
if __name__ == '__main__':
    while True:
        fibonachi()
        answer = input("Press 'Q' to quit")
        if answer.lower() == 'q':
            break
        else:
            continue
