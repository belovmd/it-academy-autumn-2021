import re


"""Вводится строка. Требуется удалить из нее повторяющиеся символы и все
    пробелы. Например, если было введено "abc cde def", то должно быть
    выведено "abcdef".
   Подсказка: оператор in проверяет, входит ли подстрока в строку или нет.
"""


def sub_string():
    """Конструирование подстроки.

    :param str_: входная строка

    :return: строка. Получившееся выражение
    """

    str_ = input("Введите выражение:")
    text = re.sub(r'[^а-яА-Я\w]', '', str_)
    text = list(text)

    new_list = []
    for char in text:
        if char not in new_list:
            new_list.append(char)

    str_output = ""
    str_output = str_output.join(new_list)
    return str_output


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    print(sub_string())
