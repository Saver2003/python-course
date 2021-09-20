from operator import itemgetter

contacts = [
    {
        "name": "John",
        "phone": "123456"
    },
    {
        "name": "Jane",
        "phone": "564321"
    },
    {
        "name": "Bob",
        "phone": "+1234"
    },
]


def show_contact(contact):
    print('{:<15}{:<15}'.format(contact['name'], contact['phone']))


def find(value):
    for contact in contacts:
        if contact['name'].lower() == value.lower() or contact['phone'].lower() == value.lower():
            return contact
    print("Контакт не найден!")


def command_list():
    print('{:<15}{:<15}'.format('Name', 'Phone'))
    for i in contacts:
        show_contact(i)


def command_find():
    search_value = input('Введите имя или номер контакта > ').lower()

    contact = find(search_value)

    if not contact:
        return

    show_contact(contact)


def command_add():
    contacts.append(
        {
            'name': input('Введите имя контакта > '),
            'phone': input('Введите номер контакта > ')
        }
    )
    commands['list']()


def command_edit():
    name = input('Введите имя контакта > ').lower()

    contact = find(name)

    if not contact:
        return

    name = input('Введите  новое имя контакта > ')
    if name:
        contact['name'] = name
    phone = input('Введите новый номер контакта > ')
    if phone:
        contact['phone'] = phone

    commands['list']()


def command_delete():
    name = input('Введите имя контакта > ').lower()

    contact = find(name)
    if not contact:
        return
    contacts.remove(contact)
    commands['list']()


def command_sort():
    print('{:<15}{:<15}'.format('Name', 'Phone'))
    newlist = sorted(contacts, key=itemgetter('name'))
    for i in newlist:
        show_contact(i)


def command_exit():
    exit('До свидания!')


commands = {
    'list': command_list,
    'find': command_find,
    'add': command_add,
    'edit': command_edit,
    'delete': command_delete,
    'sort': command_sort,
    'exit': command_exit
}

while True:
    command = input(
        "Телефонная книга. Для действия введите команду:\nlist, find, add, edit, delete, sort, exit > ")

    commands[command]()
