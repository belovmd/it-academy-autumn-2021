import re


def remove_duplicate():
    text = input("Введите выражение")
    text = re.sub(r'[^а-яА-Я\w]', '', text)
    text = text.replace(" ", "")
    text = list(text)

    new_list = []
    for char in text:
        if char not in new_list:
            new_list.append(char)

    str_output = ""
    str_output = str_output.join(new_list)
    print(str_output)


if __name__ == '__main__':
    remove_duplicate()
