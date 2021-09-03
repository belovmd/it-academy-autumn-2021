import math
import re
import string

"""Complete the solution so that it reverses the string passed into it."""


def solution(str_):
    str_ = input("Type a word:")
    str_len = len(str_)
    str_inv = str_[::-1]
    return f"'{str_}' => '{str_inv}'"


"""Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
For example, if we run 9119 through the function, 811181 will come out.
Note: The function accepts an integer and returns an integer"""


def square_digits(num):
    num = input("Type a number:")
    num = str(num)
    data = []
    for n in num:
        data.append(str(pow(int(n), 2)))
    num_new = int("".join(data))
    return num_new


"""In this kata you are required to, given a string,
replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.
"a" = 1, "b" = 2, etc.
Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
(as a string)"""


def alphabet_position(text):
    text = input("Type a sentence:")
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', '', text)
    alpha = list(string.ascii_lowercase)

    position = []
    for letter in text:
        if letter in alpha:
            position.append(alpha.index(letter) + 1)
    output = ' '.join(str(n) for n in position)
    return output


"""Сам себе придумал задачу: написать скрипт,
который находит решения квадратного уравнения,
коэффициенты которого задает пользователь"""


def square_equation(a, b, c):
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))

    d = pow(b, 2) - 4 * a * c
    if d == 0:
        x1 = x2 = -b / (2 * a)
    elif d > 0:
        x1 = (-b + math.sqrt(d) / (2 * a))
        x2 = (-b - math.sqrt(d) / (2 * a))
    elif d < 0:
        x1 = complex(-b / 2 * a, math.sqrt(abs(d)) / (2 * a))
        x2 = complex(-b / 2 * a, - math.sqrt(abs(d)) / (2 * a))
    return x1, x2


"""Be u(n) a sequence beginning with:
u[1]  = 1,  u[2]  = 1,  u[3]  = 2,  u[4]  = 3,  u[5]  = 3,  u[6] = 4,
u[7]  = 5,  u[8]  = 5,  u[9]  = 6,  u[10] = 6,  u[11] = 6,  u[12] = 8,
u[13] = 8,  u[14] = 8,  u[15] = 10, u[16] = 9,  u[17] = 10, u[18] = 11,
u[19] = 11, u[20] = 12, u[21] = 12, u[22] = 12, u[23] = 12 etc...

How is u[8] calculated?
We have u[7] = 5 and u[6] = 4. These numbers tell us that we have to go backwards
from index 8 to index 8 - 5 = 3 and to index 8 - 4 = 4 so to index 3 and 4.
u[3] = 2 and u[4] = 3 hence u[8] = u[3] + u[4] = 2 + 3 = 5.

Another example: let us calculate u[13]. At indexes 12 and 11 we have 8 and 6.
Going backwards of 8 and 6 from 13 we get indexes 13 - 8 = 5 and 13 - 6 = 7.
u[5] = 3 and u[7] = 5 so u[13] = u[5] + u[7] = 3 + 5 = 8 .

Task
1. Express u(n) as a function of n, u[n - 1], u[n - 2]. (not tested).

2. Given two numbers n, k (integers > 2) write the function length_sup_u_k(n, k)
or lengthSupUK or length-sup-u-k returning the number of terms u[i] >= k with 1 <= i <= n.
If we look above we can see that between u[1] and u[23] we have four u[i]
greater or equal to 12: length_sup_u_k(23, 12) => 4

3. Given n (integer > 2) write the function comp(n) returning the number of
times where a term of u is less than its predecessor up to and including u[n].

Examples:
u(900) => 455 (not tested)
u(90000) => 44337 (not tested)

length_sup_u_k(23, 12) => 4
length_sup_u_k(50, 10) => 35
length_sup_u_k(500, 100) => 304

comp(23) => 1 (since only u(16) < u(15))
comp(100) => 22
comp(200) => 63
"""


def length_sup_u_k(n):
    n = int(input("Enter n > 2: "))
    k = int(input("Enter k > 2: "))
    u = [1, 1]
    f = 2
    p = 0
    while f <= n - 1:
        u.append(u[f - u[f - 1]] + u[f - u[f - 2]])
        if u[f] >= k:
            p += 1
        f += 1
    return p


def comp(n):
    n = int(input("Enter n > 2: "))
    u = [1, 1]
    f = 2
    q = 0
    while f <= n - 1:
        u.append(u[f - u[f - 1]] + u[f - u[f - 2]])
        if u[f] < u[f - 1]:
            q += 1
        f += 1
    return q


if __name__ == '__main__':
    str_ = ""
    print(solution(str_))
    num = ""
    print(square_digits(num))
    text = ""
    print(alphabet_position(text))
    a, b, c = '', '', ''
    print(square_equation(a, b, c))
    n = ''
    k = ''
    print(length_sup_u_k(n))
    print(comp(n))
