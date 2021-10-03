fh = open(r'D:\python\it-academy-autumn-2021\src\homework5\data_hw5\ratings.list', 'r')
text = fh.read()
result = text.split('ТОП250 фильмов')
print(result)
