"""
4. В файле хранятся данные с сайта IMDB. Скопированные данные хранятся
   в файле ./data_hw5/ ratings.list.
a. Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
b. Найдите ТОП250 фильмов и извлеките заголовки.
c. Программа создает 3 файла
   top250_movies.txt – названия файлов (фильмов?),
   ratings.txt – гистограмма рейтингов,
   years.txt – гистограмма годов.
Задачу поместите в файл task4.py в папке src/homework5.
"""


file_name = 'ratings.list'

try:
    file1 = open(file_name, 'r')
except FileNotFoundError:
    print('Файл', file_name, 'не найден!')
else:
    print('Файл', file_name, 'успешно открыт')

    top_films = []
    i_str = 0
    while i_str < 279:
        line = file1.readline()
        if not line:
            break
        if 27 < i_str < 278:
            top_films.append(line.strip())

        i_str += 1
    file1.close

    for i in range(len(top_films)):
        top_films[i] = top_films[i].split()

    # top250_movies.txt

    top250 = []
    max_length = 0
    for i in range(len(top_films)):
        top250.append(top_films[i][3:-1])
        top250[i] = ' '.join(top250[i])
        if len(top250[i]) > max_length:
            max_length = len(top250[i])

    with open('top250_movies.txt', 'w') as f_top250:
        for i in range(len(top250)):
            f_top250.write(top250[i] + '\n')

    print('Файл top250_movies.txt успешно записан')

    ratings = []

    def draw_rating(rank):
        str_rating = '*' * round(rank * 2)  # * 2 для увеличения масштаба гистограмм
        return str_rating

    for i in range(len(top_films)):
        line_after_film = '  ' + '-' * (68 - len(top250[i]))
        ratings.append(top250[i] + line_after_film + ' ' + top_films[i][2]
                       + ' : ' + draw_rating(float(top_films[i][2])))

    with open('ratings.txt', 'w') as f_ratings:
        for i in range(len(ratings)):
            f_ratings.write(ratings[i] + '\n')

    print('Файл ratings.txt успешно записан')

    # years.txt – гистограмма годов

    years = []
    for i in range(len(top_films)):
        year_str = top_films[i][-1][1:5]
        years.append(year_str)

    years_set = set(years)
    years_dict = dict.fromkeys(years_set, 0)

    for i in range(len(years)):
        years_dict[years[i]] = years_dict.get(years[i]) + 1

    list_keys = list(years_dict.keys())
    list_keys.sort()

    with open('years.txt', 'w') as f_years:
        for el in list_keys:
            str_to_write = str(el + ' : ' + str(years_dict[el]) + ' '
                               + draw_rating(years_dict[el]) + '\n')
            f_years.write(str_to_write)

    print('Файл years.txt успешно записан')
