import re

"""Найти самое длинное слово в введенном предложении.
    В случае если их несколько, самое левое в строке Учтите что в предложении
    есть знаки препинания.
"""


def longest_word():
    """Поиск самого длинного слова в предложении.

    :param str_: входная строка

    :return: строка. Самое длинное слово в предложении (в случае если их
        несколько, самое левое в строке).
    """

    str_ = input("Введите предложение: ")
    str_new = re.sub(r'[^а-яА-Я\w\s]', '', str_)
    str_new = str_new.split()

    max_length = max(len(word) for word in str_new)
    list_words = []
    for word in str_new:
        if len(word) == max_length:
            list_words.append(word)
    print("Саммые длинные слова:")

    for word in list_words:
        print("\t%s - %d букв" % (word, len(word)))


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    longest_word()
