"""Слова
Во входной строке записан текст. Словом считается последовательность
непробельных символов идущих подряд, слова разделены одним или большим
числом пробелов или символами конца строки (\n). Определите, сколько различных
слов содержится в этом тексте.
"""

import re

str_ = "A bad workman always blames his tools. Actions speak louder than words." \
       "A chain is only as strong as its weakest link."
str_new = re.sub(r'[^\w\s]', ' ', str_)
lst = str_new.split()
print(len(lst))
