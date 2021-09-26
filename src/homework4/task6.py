# Во входной строке записан текст.
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки (\n).
# Определите, сколько различных слов содержится в этом тексте.

def convert_str(str_):
    for el in str_:
        if el == '\n':
            str_ = str_.replace(el, ' ')
    while '  ' in str_:
        str_ = str_.replace('  ', ' ')
    str_ = str_.lower()
    str_ = str_.strip()
    str_ = str_.split(' ')
    return str_


sentence = ' Словом считается последовательность   \n'\
           '  Словом последовательность'
obj = convert_str(sentence)
print('Количество различных слов в этом тексте: ', len(set(obj)))
