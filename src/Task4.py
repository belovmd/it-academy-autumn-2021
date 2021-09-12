import re

path = "/Users/Roman/Desktop/IT-academy-2021/ratings.list"

with open(path, 'r', encoding="Windows-1252") as f:
    find = "top 250"
    lst_ = f.readlines()
    lst_new = []
    index = n = 0
    flag = False
    for el in lst_:
        index += 1
        if find in el:
            print(el, "=>", index)
            n = index
            flag = True
        if flag and index < n + 252:
            lst_new.append(lst_[index].lstrip())
    for l in lst_new:
        print(l, end="")

    print("-"*30)
    lst_new2 = lst_new[lst_new.index("New  Distribution  Votes  Rank  Title\n") + 1:]
    print(lst_new2)
    print("-" * 30)
    lst_new3 = list(map(lambda x: re.split(r"\s{2,}", x), lst_new2))
    print(lst_new3)

with open("top250_movies.txt", 'w') as f1:
    for el in lst_new3:
        f1.write(el[-1])

with open("ratings.txt", 'w') as f2:
    f2.write("Comment: Five asterix for 8.0 points, for every 0.1 point one asterix is added.\n\n")
    for el in lst_new3:
        rating = int(float(el[-2])*10 - 75)*"*" + "\n"
        f2.write(f"{el[-2]} => {rating}")

with open("years.txt", 'w') as f3:
    f3.write("Comment: one film stands for one '+'.\n\n")
    dct = {}
    for el in lst_new3:
        year = el[-1][-6:-2]
        dct[year] = dct.get(year, 0) + 1
        year_rating = "%s:%s\n" % (year, int(dct[year])*"+")
        f3.write(year_rating)


