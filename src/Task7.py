import re

"""Задача на скобки"""

str_ = "[(word[world]()dinosaurs){some_text}]{}9(просто текст[{чат}][()])"
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

D_s_b_right = [k for k, v in D.items() if v == '[']
D_s_b_left = [k for k, v in D.items() if v == ']']
D_b_right = [k for k, v in D.items() if v == '{']
D_b_left = [k for k, v in D.items() if v == '}']
D_p_right = [k for k, v in D.items() if v == '(']
D_p_left = [k for k, v in D.items() if v == ')']

list_ = [D_s_b_right, D_s_b_left, D_b_right, D_b_left, D_p_right, D_p_left]
for el in list_:
    print(el)

s_b_diff = {}
for b in D_s_b_left:
    for a in D_s_b_right:
        s_b_diff[(a, b)] = abs(a - b)
        print(s_b_diff)
    D_s_b_new = {k: v for k, v in s_b_diff.items() if v == min(s_b_diff.values())}
    print(D_s_b_new)
    s_b_diff = {}

i = 0
for i in range(len(D_s_b_right)):
    if (D_s_b_left[i] - D_s_b_right[i] - 1) % 2:
        print("Квадратные скобки расставлены неверно!")

k = 0
for k in range(len(D_b_right)):
    if (D_b_left[k] - D_b_right[k] - 1) % 2:
        print("Фигурные скобки расставлены неверно!")

j = 0
for j in range(len(D_p_right)):
    if (D_p_left[j] - D_p_right[j] - 1) % 2:
        print("Обычные скобки расставлены неверно!")

print(0%2)

