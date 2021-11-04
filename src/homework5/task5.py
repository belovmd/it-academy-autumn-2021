# Написать программу которая находит ближайшую степень двойки к введенному числу.
# 10(8), 20(16), 1(1), 13(16)

def two_nearest_multiple(num):
    diff = 0
    pow = 2
    multiples = []
    # create list of power of two
    for x in range(num):
        pow = (pow << 1)
        multiples.append(pow)
    dct = {x: diff for x in multiples}
    # update the value of difference so that it shows the actual value
    for el in range(len(multiples)):
        diff = abs(multiples[el] - num)
        dct[multiples[el]] = diff
    for multiple, module in dct.items():
        if module == min(dct.values()):
            print(multiple)


two_nearest_multiple(30)
