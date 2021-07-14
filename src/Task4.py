import re


def count_letters():
    text = input("Введите выражение латиницей:")
    text = re.sub(r'[^a-zA-Z]', '', text)
    text = list(text)
    print(text)
    print(type(text))

    letters_uppercase = []
    letters_lowercase = []
    my_str = ""

    for letter in text:
        if letter.isupper():
            letters_uppercase.append(letter)
        elif letter.islower():
            letters_lowercase.append(letter)

    print(
        "В тексте содержится %i букв в верхнем регистре: %s" % (len(letters_uppercase), my_str.join(letters_uppercase)))
    print(
        "В тексте содержится %i букв в нижнем регистре: %s" % (len(letters_lowercase), my_str.join(letters_lowercase)))


if __name__ == '__main__':
    count_letters()
