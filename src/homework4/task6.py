"""
Во входной строке записан текст. Словом считается последовательность
непробельных символов идущих подряд, слова разделены одним или большим
числом пробелов или символами конца строки (\n). Определите,
сколько различных слов содержится в этом тексте.
"""

str_ = 'Здравствуй, милая, безнадежная,\n мои слонце, и любовь, и грусть.'

for element in '\n.,:;!?/@№#$%^&*()_-=+`~':
    if element in str_:
        str_ = str_.replace(element, ' ')
list_of_words = str_.split()

import collections

dct_of_words = collections.Counter()
for word in list_of_words:
    dct_of_words[word] += 1

print(len(list(dct_of_words)))
