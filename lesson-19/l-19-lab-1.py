from typing import List, Optional
import json


class Contact:
    def __init__(self, name, phone_number) -> None:
        self.name = name
        self.phone_number = phone_number

    def print_contact(self):
        print(f'{self.name:<25}{self.phone_number:>15}')

    def to_dict(self):
        return {
            'name': self.name,
            'phone_number': self.phone_number
        }


class Phonebook:
    def __init__(self, contacts: List[Contact] = []) -> None:
        self.contacts = contacts

    def print_contacts(self):
        print('{:<25}{:>15}'.format('Имя', 'Телефон'))
        for contact in self.contacts:
            contact.print_contact()

    def add_contact(self, contact: Contact):
        self.contacts.append(contact)

    def find_contact(self, name: str) -> Optional[Contact]:
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None

    def edit_contact(self, contact: Contact):
        new_name = input('Введите новое имя контакта: ')
        new_phone_number = input('Введите новый номер: ')
        contact.name = new_name
        contact.phone_number = new_phone_number

    def delete_contact(self, name: str):
        contact = self.find_contact(name)
        self.contacts.remove(contact)

    def sort_contacts(self):
        sorted_contacts = sorted(self.contacts, key=lambda item: item.name)
        for contact in sorted_contacts:
            contact.print_contact()


class Application:
    def __init__(self) -> None:
        self.phonebook = None
        self.load_from_file()

        self.commands = {
            'list': self.phonebook.print_contacts,
            'exit': self.command_exit,
            'add': self.command_add_contact,
            'find': self.command_find,
            'edit': self.command_edit_contact,
            'delete': self.command_delete_contact,
            'sort': self.command_sort
        }

    def command_add_contact(self):
        name = input("Введите имя контакта: ")
        if self.phonebook.find_contact(name):
            print('Такой контакт уже есть!')
            return
        phone_number = input('Введите номер телефона: ')

        contact = Contact(name, phone_number)
        self.phonebook.add_contact(contact)

        self.save_to_file()

    def command_edit_contact(self):
        name = input('Введите имя контакта: ')
        contact = self.phonebook.find_contact(name)
        self.phonebook.edit_contact(contact)
        self.save_to_file()

    def command_delete_contact(self):
        name = input('Введите имя контакта: ')
        self.phonebook.delete_contact(name)
        self.save_to_file()

    def command_find(self):
        contact_name = input('Введите имя контакта: ')
        contact = self.phonebook.find_contact(contact_name)
        print('{:<25}{:>15}'.format('Имя', 'Телефон'))
        contact.print_contact()

    def command_sort(self):
        self.phonebook.sort_contacts()

    def load_from_file(self):
        with open('contacts.txt', 'r') as f:
            contacts = []
            for contact_data in json.load(f):
                contact = Contact(
                    contact_data['name'], contact_data['phone_number'])
                contacts.append(contact)
            self.phonebook = Phonebook(contacts)

    def save_to_file(self):
        with open('contacts.txt', 'w') as f:
            preparing_contacts = [c.to_dict() for c in self.phonebook.contacts]
            json.dump(preparing_contacts, f)

    def run(self):
        while True:
            command = input(
                "Телефонная книга. Для действия введите команду:\nlist, find, add, edit, delete, sort, exit > ").strip().lower()

            if command == 'list' or command == 'exit' or command == 'add' or command == 'find' or command == 'edit' or command == 'delete' or command == 'sort':
                self.commands[command]()
            else:
                print('Нет такой команды!')

    def command_exit(self):
        exit("До свидания!")


app = Application()

app.run()
