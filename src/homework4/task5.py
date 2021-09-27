# Каждый из N школьников некоторой школы знает Mi языков.
# Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.

language = []
n = int(input("Введите количество школьников"))
for _ in range(n):
    m = int(input("Введите колличество языков которые знает школьник"))
    lang_lst = set()
    for _ in range(m):
        lang_lst.add(input("Введите языки которые знает школьник"))
    language.append(lang_lst)

all_knows = set.intersection(*language)
all_langs = set.union(*language)


print("Хотя бы один из школьников знает", all_langs,)
print("Все школьники знают", all_knows)
