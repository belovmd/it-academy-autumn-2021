'''6. Слова
    Во входной строке записан текст.
    Словом считается последовательность непробельных символов идущих подряд,
    слова разделены одним или большим числом пробелов или символами конца строки.
    Определите, сколько различных слов содержится в этом тексте.
'''

str_ = 'Это строка  введена в качестве примера!\nНикакой смысловой нагрузки в себе не несет.'
print('Количество различных слов в тексте: ', len(set(str_.split())))
