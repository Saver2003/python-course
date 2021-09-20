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
    }
]


def show_movie(movie):
    print('{:<35}{:<15}'.format(movie['name'], 'rating'))


def command_add():
    movies.append({
        'name': input("Введите название фильма > "),
        'ratings': {}
    })


def command_delete():
    print('delete')


def command_list():
    print('{:<35}{:<15}'.format('Movie', 'Rating'))
    for i in movies:
        show_movie(i)


def command_rate():
    print('rate')


def command_find():
    print('find')


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


def check_command(command):
    if command in commands:
        print("Нет такой команды")


while True:
    command = input("Введите команду: add, delete, list, rate, find, exit > ")
    if not command in commands:
        print("Нет такой команды")
    else:
        commands[command]()