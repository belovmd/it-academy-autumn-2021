import re

"""Задача на скобки"""

str_ = "[(word[world](){dinos}au{rs}){some_text}]{}9(просто текст[{чат}][()])"
str_new = re.sub(r'[^()\[\]{}]', '', str_)
print(str_new)
s_b_right = str_new.count('[')
s_b_left = str_new.count(']')
b_right = str_new.count('{')
b_left = str_new.count('}')
p_right = str_new.count('(')
p_left = str_new.count(')')

if s_b_right != s_b_left or b_right != b_left or p_right != p_left:
    print("Скобки расставлены неверно:")
    print(f"Square braces: {s_b_right} != {s_b_left}")
    print(f"Braces: {b_right} != {b_left}")
    print(f"Parentheses: {p_right} != {p_left}")
else:
    print("Количество всех скобок верное!")

D = {}
for k, v in zip(range(len(str_new)), str_new):
    D[k] = v
print(D)

D_s_b_right = [k for k, v in D.items() if v == '[']
D_s_b_left = [k for k, v in D.items() if v == ']']
D_b_right = [k for k, v in D.items() if v == '{']
D_b_left = [k for k, v in D.items() if v == '}']
D_p_right = [k for k, v in D.items() if v == '(']
D_p_left = [k for k, v in D.items() if v == ')']

list_ = [D_s_b_right, D_s_b_left, D_b_right, D_b_left, D_p_right, D_p_left]
for el in list_:
    print(el)

s_b_diff_list = []
for b in D_s_b_left:
    for a in D_s_b_right:
        s_b_diff_list.append(abs(a - b))
        s_b_diff_list.sort()
        s_b_diff_list = s_b_diff_list[:len(D_s_b_left)]
print(s_b_diff_list)

for el in s_b_diff_list:
    if el != 1 and not el % 2:
        print("Квадратные скобки расставлены неверно!")
    else:
        print("Квадратные скобки расставлены верно!")

b_diff_list = []
for c in D_b_left:
    for d in D_b_right:
        b_diff_list.append(abs(d - c))
        b_diff_list.sort()
        b_diff_list = b_diff_list[:len(D_b_left)]
print(b_diff_list)

for el in b_diff_list:
    if el != 1 and not el % 2:
        print("Фигурные скобки расставлены неверно!")
    else:
        print("Фигурные скобки расставлены верно!")


p_diff_list = []
for f in D_p_left:
    for e in D_p_right:
        p_diff_list.append(abs(e - f))
        p_diff_list.sort()
        p_diff_list = p_diff_list[:len(D_p_left)]
print(p_diff_list)

for el in p_diff_list:
    if el != 1 and not el % 2:
        print("Обычне скобки расставлены неверно!")
    else:
        print("Обычные скобки расставлены верно!")