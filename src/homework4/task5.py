'''Каждый из N школьников некоторой школы знает Mi языков. Определите,
какие языки знают все школьники и языки, которые знает хотя бы один из школьников.'''

n = int(input("Сколько школьников"))
c = []
for range in range(n):
    b = set(input("языки школоты").split())
    c.append(b)
one = c[0]
al = c[0]
for a in c:
    al = al.intersection(a)
    one = one.union(a)
print("Все школьники знают", al)
print("Хотя бы один школьник знает", one)
