import re

"""Посчитать количество строчных (маленьких) и прописных (больших) букв в
    введенной строке. Учитывать только английские буквы.
"""


def count_letters(_str):
    """Подсчет символов.
        :param str_: входная строка
        :return: кортеж. (low_number, up_number). low_number - количество строчных,
                                                  up_number - количество пописных.
        """

    text = input("Введите выражение латиницей:")
    text = re.sub(r'[^a-zA-Z]', '', text)
    text = list(text)

    letters_uppercase = []
    letters_lowercase = []

    for letter in text:
        if letter.isupper():
            letters_uppercase.append(letter)
        elif letter.islower():
            letters_lowercase.append(letter)

    output1 = "В предложении содержится %i букв в верхнем регистре." % (len(letters_uppercase))
    output2 = "В предложении содержится %i букв в нижнем регистре." % (len(letters_lowercase))

    return output1, output2


if __name__ == '__main__':
    str_ = ''
    print(count_letters(str_))


