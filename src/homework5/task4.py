import matplotlib.pyplot as plt


with open(r'D:\python\it-academy-autumn-2021\src\homework5\data_hw5\ratings.list', 'r') as fh:
    list_file = fh.readlines()
    i = req_line = 0
    target_list = []

    # Найдите ТОП250 фильмов и извлеките заголовки.
    for line in list_file:
        i += 1
        # determining the required line
        if 'note: for this top 250, only votes from regular voters are considered.' in line:
            req_line = i
        if 28 < i < 279:
            target_list.append(line.strip())
    for el in range(len(target_list)):
        target_list[el] = target_list[el].split()

    # Программа создает 3 файла
    # top250_movies.txt – названия файлов,

    TOP250 = []
    for line in range(len(target_list)):
        TOP250.append(target_list[line][3:-1])
        TOP250[line] = ' '.join(TOP250[line])

    with open(r'D:\python\it-academy-autumn-2021\src\homework5\data_hw5\top250_movies.txt',
              'w') as top_movies:
        i = 1
        for movie in TOP250:
            top_movies.write(str(i) + '.' + ' ' + str(movie) + '\n')
            i += 1

    # ratings.txt – гистограмма рейтингов,
    ratings = []
    for el in range(len(target_list)):
        ratings.append(target_list[el][2])

    plt.hist(ratings, bins=50,
             histtype='bar',
             color='blue',)

    plt.xticks(rotation=45, fontsize=3)
    plt.title('Ratings',
              fontweight="bold")
    plt.savefig('ratings.png')

    # years.txt – гистограмма годов.
    years = []
    for el in range(len(target_list)):
        years.append(target_list[el][-1])

    plt.hist(years, bins=150,
             histtype='bar',
             color='blue',)

    plt.xticks(rotation=45, fontsize=3)

    plt.title('Years', fontweight="bold")

    plt.savefig('years.png')
