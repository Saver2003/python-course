from operator import itemgetter

contacts = []


def read_contacts_from_file():
    with open('./phone-book.txt', 'r') as f:
        for raw_contact_data in f.readlines():
            contact_data = {}
            for raw_key_value_data in raw_contact_data.split('='):
                key, value = raw_key_value_data.split(':')
                contact_data[key] = value.rstrip()
            contacts.append(contact_data)


read_contacts_from_file()


def write_contact_to_file(contacts_to_write):
    with open('./phone-book.txt', 'w') as f:
        contacts_data = []
        for contact in contacts_to_write:
            contact_data = []
            for key, value in contact.items():
                contact_data.append(f'{key}:{value}')
            contacts_data.append('='.join(contact_data))
        f.write('\n'.join(contacts_data))


def show_contact(contact):
    print('{:<15}{:<15}'.format(contact['name'], contact['phone']))


def find(value):
    for contact in contacts:
        if contact['name'].lower() == value.lower() or contact['phone'].lower() == value.lower():
            return contact
    print("Контакт не найден!")


def command_list():
    print('{:<15}{:<15}'.format('Name', 'Phone'))
    for i in sorted(contacts, key=lambda item: item['name']):
        show_contact(i)


def command_find():
    search_value = input('Введите имя или номер контакта > ').lower()

    contact = find(search_value)

    if not contact:
        return

    show_contact(contact)


def command_add():
    contact_name = input('Введите имя контакта > ')
    contact_phone = input('Введите номер контакта > ')
    if contact_name.find(',') == -1:
        contacts.append(
            {
                'name': contact_name,
                'phone': contact_phone
            }
        )
    commands['list']()
    write_contact_to_file(contacts)


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
    write_contact_to_file(contacts)


def command_delete():
    name = input('Введите имя контакта > ').lower()

    contact = find(name)
    if not contact:
        return
    contacts.remove(contact)
    commands['list']()
    write_contact_to_file(contacts)


def command_sort():
    print('{:<15}{:<15}'.format('Name', 'Phone'))
    newlist = sorted(contacts, key=lambda item: item['name'])
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
