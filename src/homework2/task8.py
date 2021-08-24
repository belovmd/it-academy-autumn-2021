''' 1.
    https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python

    Your task is to make a function that can take any non-negative integer
    as an argument and return it with its digits in descending order.
    Essentially, rearrange the digits to create the highest possible number.
    Examples:
    Input: 42145 Output: 54421
    Input: 145263 Output: 654321
    Input: 123456789 Output: 987654321
'''

chislo = int(input('Введите число:'))
list_ = [int(x) for x in str(chislo)]
list_.sort(reverse=True)
new_s = ''.join(str(a) for a in list_)
print(new_s)


''' 2.
    https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python

    The goal of this exercise is to convert a string to a new string
    where each character in the new string is "("
    if that character appears only once in the original string,
    or ")" if that character appears more than once in the original string.
    Ignore capitalization when determining if a character is a duplicate.
    Examples:
    "din"      =>  "((("
    "recede"   =>  "()()()"
    "Success"  =>  ")())())"
    "(( @"     =>  "))(("
'''

str_ = input('Введите строку: ')
result = []
for i in str_.lower():
    if str_.count(i) > 1:
        result.append(')')
    else:
        result.append('(')
print(''.join(str(_) for _ in result))


''' 3.
    "Учебное пособие для 9 класса", В.М. Котов, пример 8.4.

    Написать программу, которая выводит на экран последний символ введенного слова
    и определяет, встречается ли этот символ в слове еще раз,
    если встречается, то программа выводит индекс символа.
'''

a = input('Введите слово:')
print('Последний символ', a[-1])
b = a.find(a[-1])
if b == len(a):
    print(b)


''' 4.
    https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python

    Write a function that takes a string of parentheses,
    and determines if the order of the parentheses is valid.
    The function should return true if the string is valid,
    and false if it's invalid.
    Examples
    "()"              =>  true
    ")(()))"          =>  false
    "("               =>  false
    "(())((()())())"  =>  true
'''

def parentheses():
    str_ = input('Введите строку: ')
    result = (str_.count('(') == str_.count(')') and
              str_.count('[') == str_.count(']') and
              str_.count('{') == str_.count('}') and
              str_.count('<') == str_.count('>'))
    return result


print(parentheses())


''' 5.
    https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/python

    You might know some pretty large perfect squares. But what about the NEXT one?
    Complete the findNextSquare method that finds the next integral perfect square
    after the one passed as a parameter.
    Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
    If the parameter is itself not a perfect square then -1 should be returned.
    You may assume the parameter is non-negative.
    Examples:
    findNextSquare(121) --> returns 144
    findNextSquare(625) --> returns 676
    findNextSquare(114) --> returns -1 since 114 is not a perfect
'''

a = int(input())
if a**0.5 == int(a**0.5):
    b = (a**0.5 + 1)**2
    print(int(b))
else:
    print('-1')
