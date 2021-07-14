import re


def longest_word():

    text = input('Введите предложение:')
    text_new = re.sub(r'[^а-яА-Я\w\s]', '', text)
    text_new = text_new.split()

    max_length = len(text_new[0])
    for word in text_new:
        if len(word) >= max_length:
            max_length = len(word)
            max_word = word

    list_words = []
    for word in text_new:
        if len(word) == max_length:
            list_words.append(word)

    print("Саммые длинные слова:")
    for word in list_words:
        print("\t%s - %d букв" % (word, len(word)))


if __name__ == '__main__':
    while True:
        longest_word()
        answer = input("Нажмите Q чтобы выйти")
        if answer.lower() == 'q':
            break
        else:
            continue
