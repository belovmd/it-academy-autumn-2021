# В файле хранятся данные с сайта IMDB.
# Скопированные данные хранятся в файле ./data_hw5/ ratings.list.
# a. Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
# b. Найдите ТОП250 фильмов и извлеките заголовки.
# c. Программа создает 3 файла  top250_movies.txt – названия файлов,
# ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов

import matplotlib.pyplot as plt
import pandas

reader = open('ratings.list', 'r')

line = reader.readline()
while line == '\n' or 'New' not in line and 'Distribution' not in line:
    line = reader.readline()

line = reader.readline()
ratings = []
years = []
while line != '' and line != '\n' and line != 'BOTTOM 10 MOVIES (1500+ VOTES)':
    columns = line.split()
    index = len(columns[0]) + len(columns[1]) + len(columns[2]) + 13
    title = line[index:len(line)]

    with open('top250_movies.txt', 'a') as writer:
        line = title + '\n'
        writer.write(line)

    ratings.append(columns[2])

    year = line[(line.index('(') + 1):line.index(')')]
    years.append(year)
    years.sort()

    line = reader.readline()

rate_hist = plt.hist(ratings, bins=10)
plt.title('Ratings')
plt.xlabel('Ratings')
plt.ylabel('Movies count')
ys = rate_hist[0]
xs = rate_hist[1]
plt.savefig('ratings.png')

year_hist = plt.hist(years, bins=10)
plt.title('Years')
plt.xlabel('Years')
plt.xticks(rotation=90, fontsize=4)
plt.ylabel('Movies count')
ys = year_hist[0]
xs = year_hist[1]
plt.savefig('years.png')

reader.close()
