''' В файле хранятся данные с сайта IMDB.
    Скопированные данные хранятся в файле ./data_hw5/ ratings.list.
    Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
    Найдите ТОП250 фильмов и извлеките заголовки.
    Программа создает 3 файла
    top250_movies.txt – названия файлов,
    ratings.txt – гистограмма рейтингов,
    years.txt – гистограмма годов.
'''

import re

DATA_START_LINE_NUMBER = 29
DATA_END_LINE_NUMBER = 278


def histogram(lst_):
    lst_.sort()
    result = ''
    histogram_dct = {}
    for elem in lst_:
        histogram_dct[elem] = histogram_dct.get(elem, '') + '*'
    for key, value in histogram_dct.items():
        result += f'{key}: {value}\n'
    return result


try:
    with open('ratings.list.txt') as fh:
        data = fh.readlines()
        index = 0
        top_250 = []
        ratings = []
        years = []

        for element in data:
            index += 1
            if index >= DATA_START_LINE_NUMBER:
                top_250 += re.findall(r'(?<=\d\.\d\s{2}).+(?=\s\()', element)
                ratings += re.findall(r'\d\.\d', element)
                years += re.findall(r'(?<=\()\d{4}', element)

            if index == DATA_END_LINE_NUMBER:
                break

    years_histogram = histogram(years)
    ratings_histogram = histogram(ratings)

    with open('./top250_movies.txt', 'w') as movies:
        movies.write('\n'.join(top_250))
    with open('./ratings.txt', 'w') as ratings:
        ratings.write(ratings_histogram)
    with open('./years.txt', 'w') as years:
        years.write(years_histogram)

except FileNotFoundError:
    print('Файл не найден')
