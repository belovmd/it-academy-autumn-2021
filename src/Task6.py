"""Определите, является ли число палиндромом (читается слева направо и справа
    налево одинаково).  Число положительное целое, произвольной длины. Задача
    требует работать только с числами (без конвертации числа в строку или
    что-нибудь еще)
"""


def palindrom(n):
    """Поиск числа фибоначчи.
        :param n: Число.
        :return: Bool. True или False. Является ли число палиндромом.
        """

    # Проверка на то, что пользователь ввел int, если нет, то будет предложен новый ввод.
    while True:
        n = input("Введите число")
        try:
            n = int(n)
            break
        except ValueError:
            print("Нужно ввести целое число!")
            continue

    k = 10
    while (n // k) > 10:
        k *= 10

    factor = 1
    num = n
    n_reverse = 0
    while k >= 1:
        cipher = (num // k)
        n_reverse += cipher*factor
        num = num - cipher * k
        k = k / 10
        factor *= 10

    return n_reverse == n


if __name__ == '__main__':
    n = 0
    print(palindrom(n))
