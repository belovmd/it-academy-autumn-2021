"""Dict comprehensions
Создайте словарь с помощью генератора словарей, так чтобы его ключами были числа от 1 до 20, а значениями кубы этих чисел.
"""


def dict_generator():
    dict_ = {k: k**3 for k in range(21)}
    return dict_


if __name__ == '__main__':
    print(dict_generator())