# В файле хранятся данные с сайта IMDB.
# Скопированные данные хранятся в файле ./data_hw5/ ratings.list.
# Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
# Найдите ТОП250 фильмов и извлеките заголовки.
# Программа создает 3 файла  top250_movies.txt – названия файлов,
# ratings.txt – гистограмма рейтингов,
# years.txt – гистограмма годов.

import re

START = 29
END = 278


def create_histogram(lst):
    lst.sort()
    histogram_dict = {}
    histogram_str = ''
    for elem in lst:
        if elem not in histogram_dict:
            histogram_dict[elem] = ''
        histogram_dict[elem] += '+'

    for key, value in histogram_dict.items():
        histogram_str += f'{str(key)}: {value}\n'

    return histogram_str


with open('ratings.list') as rating_list:
    start = 0
    top250_movies = []
    years = []
    ratings = []

    for elem in rating_list:
        start += 1
        if start >= START:
            years += re.findall(r"(?<=\()\d{4}", elem)
            ratings += re.findall(r"\d\.\d", elem)
            top250_movies += re.findall(r"(?<=\d\.\d\s{2}).+(?=\s\()", elem)

        if start == END:
            break

    years_histogram = create_histogram(years)
    ratings_histogram = create_histogram(ratings)

    with open('./top250_movies.txt', 'w') as m:
        m.write('\n'.join(top250_movies))
    with open('./ratings.txt', 'w') as r:
        r.write(ratings_histogram)
    with open('./years.txt', 'w') as y:
        y.write(years_histogram)
