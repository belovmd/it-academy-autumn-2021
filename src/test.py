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
print(mymap(pow, [1, 2, 3], [2, 3, 4, 5]))"""

def myzip(*seqs):
    seqs = [list(S) for S in seqs]
    print(seqs)
    res = []
    while all(seqs):
        res.append(tuple(S.pop(0) for S in seqs))
    return res

print(dir(Task6))


lst_ = ['a', 'b', 'c', 'd']
dct_ = {x:y for (x, y) in enumerate(lst_)}
print(dct_)



if __name__ == '__main__':
    print(myzip([1, 2, 3], ['a', 'b', 'c']))

