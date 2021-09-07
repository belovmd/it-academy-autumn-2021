'''
Во входной строке записан текст. Словом считается последовательность непробельных
символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца
строки (\n). Определите, сколько различных слов содержится в этом тексте.
'''


str_ = "Python is an experiment in how much freedom programmers need. Too much freedom and nobody can read another's code; too little and expressiveness is endangered."
print(len(set(str_.split())))
