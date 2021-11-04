"""
Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся
целых чисел, отсортированных по возрастанию, которая этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"
Задачу поместите в файл task3.py в папке src/homework5.
"""


def get_ranges(s):

    print(s)
    roll_up = ''

    if len(s) != 1:  # если список состоит из нескольких элементов
        first = s[0]
        last = s[0]
        for i in range(1, len(s)):
            if s[i] == s[-1]:  # если очередной эл-т последний в списке
                if (last + 1) == s[i]:  # если очередной эл-т входит в последний диапазон
                    roll_up += str(first) + '-' + str(s[i])
                else:  # если очередной эл-т не входит в последний диапазон
                    if not first == last:
                        roll_up += str(first) + '-' + str(last)
                        roll_up += ',' + str(s[i])
                    else:
                        roll_up += str(last)
                        roll_up += ',' + str(s[i])
            else:  # если очередной эл-т не последний в общем списке
                if (last + 1) == s[i]:  # если очер элемент > на 1 предыдущего (и он не последний)
                    last = s[i]
                else:  # если очередной элемент выходит за текущий диапазон (и он не последний)
                    if first == last:  # если контролируемый диапазон - единичный эл-т
                        roll_up += str(last)
                    else:
                        roll_up += str(first) + '-' + str(last)

                    first = s[i]
                    last = s[i]
                    roll_up += ','

    else:  # если список состоит из одного элемента
        roll_up = str(s[0])
        
    return roll_up


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print()
print(get_ranges([4, 7, 10]))
print()
print(get_ranges([2, 3, 8, 9]))
