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


def command_exit():
    exit('До свидания!')


commands = {
    'add': None,
    'delete': None,
    'list': None,
    'rate': None,
    'find': None,
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
