"""
Посчитать количество строчных (маленьких) и прописных
(больших) букв в введенной строке. Учитывать только английские буквы.
"""

str_ = input('Input some english text: ')
let_s = 0
let_b = 0
for i in str_:
    if 'a' <= i <= 'z':
        let_s += 1
    else:
        if 'A' <= i <= 'Z':
            let_b += 1
print('Lower letters: ', let_s)
print('Upper letters: ', let_b)
