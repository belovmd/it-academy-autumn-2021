'''Во входной строке записан текст. Словом считается последовательность
непробельных символов идущих подряд, слова разделены одним или большим числом пробелов
или символами конца строки (\n). Определите, сколько различных слов содержится в этом тексте.'''

a = "i love   Milk or   git or python"
print(len(set(a.split())))
