from os import write


movies = [
]


def read_movies_from_file():
    with open('./movies-rating.txt', 'r') as f:
        list_movies = eval(f.read())
        return list_movies


movies = read_movies_from_file()


def write_movie_to_file():
    with open('./movies-rating.txt', 'w') as f:
        movie_string = str(movies)
        f.write(movie_string)


def show_movie(movie):
    ratings = movie['ratings'].values()
    rating_sum = 0
    for i in ratings:
        rating_sum += i

    if not len(ratings):
        print('{:<35}{:<15}'.format(movie['name'], 'Фильм не оценивался'))
    else:
        average_rating = rating_sum / len(ratings)
        print('{:<35}{:<15}'.format(
            movie['name'], "{0:.2f}".format(average_rating)))


def show_rating(rating):
    rating_sum = 0

    if len(rating) == 0:
        print('Фильм не оценивался')
    else:
        for i in rating.values():
            rating_sum += i
        for i in rating.items():
            print('{:<15}{:15}'.format(i[0], i[1]))
        average_rating = rating_sum / len(rating)
        print('{:<15}{:15}'.format('Средняя оценка',
              "{0:.2f}".format(average_rating)))


def find_movie(search_value):
    for movie in movies:
        if movie['name'].lower() == search_value.lower():
            return movie


def command_add():
    movies.append({
        'name': input("Введите название фильма > "),
        'ratings': {}
    })
    write_movie_to_file()


def command_delete():
    title = input("Введите название фильма > ")
    movie = find_movie(title)
    movies.remove(movie)
    commands['list']()
    write_movie_to_file()


def command_list():
    print('{:<35}{:<15}'.format('Название фильма', 'Рейтинг'))
    for movie in movies:
        show_movie(movie)


def command_rate():
    movie_title = input("Введите название фильма > ")
    name = input("Введите своё имя > ")
    rating = int(input("Введите оценку от 1 до 10 > "))

    movie = find_movie(movie_title)

    if rating > 0 and rating <= 10:
        movie['ratings'][name] = rating
    if rating == 0:
        movie['ratings'].pop(name)

    write_movie_to_file()
    show_movie(movie)


def command_find():
    title = input("Введите название фильма > ")
    movie = find_movie(title)
    # print(movie['ratings'])
    print(movie['name'])
    show_rating(movie['ratings'])


def command_exit():
    exit('До свидания!')


commands = {
    'add': command_add,
    'delete': command_delete,
    'list': command_list,
    'rate': command_rate,
    'find': command_find,
    'exit': command_exit,
}


while True:
    command = input("Введите команду: add, delete, list, rate, find, exit > ")
    if not command in commands:
        print("Нет такой команды")
    else:
        commands[command]()
