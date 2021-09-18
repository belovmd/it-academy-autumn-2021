import Task6

"""S = "spam"
for i in range(len(S)):  # Для позиций 0. .3
    x = S[i:] + S[:i] # Задняя часть + передняя часть (тот же самый эффект)
    print(S[i:], S[:i])
    print(x, end=" ")"""

"""s = "spam"

def permutel(seq):
    if not seq:
        return [seq]
    else:
        res = []
        for i in range (len (seq) ) :
            rest = seq[:i] + seq[i+1:]
            print(rest)
            for x in permutel(rest):
                res.append(seq[i:i+1] + x)
                print(res)
        return res

def permute2(seq) :
    if not seq:
        yield seq
    else:
        for i in range (len (seq) ) :
            rest = seq[:i] + seq[i+l:]
            for x in permute2 (rest) :
                yield seq[i:i+l] + x

print(permutel(s))"""

# Аналог map (func, seqs...) на основе zip
"""def mymap(func, *seqs):

    res = []
    print(list(zip(*seqs)))
    for args in zip(*seqs):
        res.append(func(*args))

    return res

print(mymap(abs, [-2, -1, 0, 1, 2]))
print(mymap(pow, [1, 2, 3], [2, 3, 4, 5]))




lst_ = ['a', 'b', 'c', 'd']
dct_ = {x:y for (x, y) in enumerate(lst_)}
print(dct_)

a = ".,af.,.gf."
print(a.strip(",."))
print(a.split(".,"))

p = [{'a': 123, 'b': 'c'}]
print(type(p))"""


c = 1,000,000
print(c)

print('1' == 1)
__str__ = 1
print(__str__)

