"""В файле хранятся данные с сайта IMDB.
Скопированные данные хранятся в файле ./data_hw5/ ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла
top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов,
years.txt – гистограмма годов.
"""


def films():
    try:
        with open('ratings.list', 'rt') as openfile:
            lines = openfile.readlines()

            lst = []
            index = 0

            for el in lines:
                index += 1
                if "New  Distribution  Votes  Rank  Title" in el:
                    break

            for num in range(250):
                lst.append(lines[index])
                index += 1

            top250_lst = []
            rating_lst = []
            year_lst = []

            for i in lst:
                sym = i.split()
                year_lst.append(sym[-1])
                rating_lst.append(sym[2])
                top250_lst.append(sym[3:-1])

            print(top250_lst)

            dct_raiting = {}
            dct_years = {}

            for s in rating_lst:
                dct_raiting[s] = dct_raiting.get(s, '') + '$'

            for s in year_lst:
                dct_years[s] = dct_years.get(s, '') + '>'

            with open('raiting.txt', 'w') as f2:
                for el, val in dct_raiting.items():
                    str_ = str(el) + str(val) + '\n'
                    f2.write(str_)

            with open('years.txt', 'w') as f3:
                for el, val in dct_years.items():
                    str_ = str(el) + str(val) + '\n'
                    f3.write(str_)

            with open('top250_movies.txt', 'w') as f1:
                for el in top250_lst:
                    str_ = ' '.join(el) + '\n'
                    f1.write(str_)

    except FileNotFoundError:
        print('ERROR')


films()
