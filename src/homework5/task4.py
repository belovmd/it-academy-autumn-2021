"""
В файле хранятся данные с сайта IMDB. Скопированные данные хранятся в файле./data_hw5/ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt – названия файлов, ratings.txt – гистограмма
рейтингов, years.txt – гистограмма годов.

"""
import sys


try:
    with open("ratings.lis1t", "rt") as fh:
        print('Файл найден, программа выполняется.')
        all_lst = fh.readlines()
except FileNotFoundError:
    print('Файл не найден!\nПрограмма остановлена!')
    sys.exit()

lst = []
index = 0

# с помощью index, считаем на какой строке начнется список фильмов
for el in all_lst:
    index += 1
    if "New  Distribution  Votes  Rank  Title" in el:
        break

# создаем список фильмов не сортированный с рейтингами и годами
for num in range(250):
    lst.append(all_lst[index])
    index += 1

title_lst = []
rating_lst = []
year_list = []

for el in lst:
    _ = el.split()
# создаем список годов фильмов, используем данный индекс тк знаем что год написан к конце списка
    year_list.append(_[-1])
# создаем список рейтингов, индекс [2], тк под этим индексом рейтинг
    rating_lst.append(_[2])
# создаем список названий фильмов, используем данные индексы [3:-1],
# тк название начинается с [3] и заканчивается предпоследним
    title_lst.append(_[3:-1])

dct_rating = {}
dct_years = {}

# Делаем гистограмму рейтингов с помощью словарей и метода get
for elem in rating_lst:
    dct_rating[elem] = dct_rating.get(elem, '') + '+'

# Делаем гистограмму годов с помощью словарей и метода get
for elem in year_list:
    dct_years[elem] = dct_years.get(elem, '') + '+'

# записываем данные гистограммы рейтингов в файл
fh_ratings = open("ratings.txt", "w")
for el, val in dct_rating.items():
    str_ = str(el) + str(val) + '\n'
    fh_ratings.write(str_)
fh_ratings.close()

# записываем данные гистограммы фильмов в файл
fh_years = open("years.txt", "w")
for el, val in dct_years.items():
    str_ = str(el) + str(val) + '\n'
    fh_years.write(str_)
fh_years.close()

# записываем список топ250 фильмов в файл
fh_title = open("top250_movies.txt", "w")
for el in title_lst:
    str_ = ' '.join(el) + '\n'
    fh_title.write(str_)
fh_title.close()
