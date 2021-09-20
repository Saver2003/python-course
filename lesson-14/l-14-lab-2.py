movies = [
    {
        'name': 'Interstellar',
        'ratings': {
            'John': 10,
            'Jack': 3
        }
    },
    {
        'name': 'Avengers: Infinity War',
        'ratings': {
            'Jack': 9,
            'Jane': 10
        }
    },
    {
        'name': 'Forrest Gump',
        'ratings': {
            'Nick': 10,
            'Mary': 10
        }
    }
]


def show_movie(movie):
    ratings = movie['ratings'].values()
    rating_sum = 0
    for i in ratings:
        rating_sum += i
    average_rating = rating_sum / len(ratings)
    print('{:<35}{:<15}'.format(movie['name'], average_rating)) # приделать вывод если у фильма нет оценки



def find_movie(search_value):
    for movie in movies:
        if movie['name'].lower() == search_value.lower():
            return movie


def command_add():
    movies.append({
        'name': input("Введите название фильма > "),
        'ratings': {}
    })


def command_delete():
    title = input("Введите название фильма > ")
    movie = find_movie(title)
    movies.remove(movie)
    commands['list']()


def command_list():
    print('{:<35}{:<15}'.format('Movie', 'Rating'))
    for movie in movies:
        show_movie(movie)


def command_rate():
    print('rate')


def command_find():
    title = input("Введите название фильма > ")
    movie = find_movie(title)


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
