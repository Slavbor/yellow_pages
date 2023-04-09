import module
import text_fields as txt


def main_menu() -> int:
    print('''Главное меню:
     1. Сохранить.
     2. Показать все контакты.
     3. Создать контакт.
     4. Найти контакт.
     5. Изменить контакт.
     6. Удалить контакт.
     7. Выход.''')
    choice = ''
    while True:
        choice = input('Введите цифру пункта меню: -> ')
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)
        else:
            print('Введено неправильное значение(введите число от 1 до 8)')


def num_to_find():
    while True:
        num_find = input(txt.contact_change)
        if num_find.isdigit() and 0 < int(num_find) <= len(module.phone_book):
            return int(num_find) - 1
        else:
            print()
            print(txt.notnumber)


def print_info(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')


def show_contacts(book: list[dict], message: str):
    if book:
        print('\n' + '=' * 60)
        for n, contact in enumerate(book, 1):
            print(f'{n}.{contact.get("name"):<20}'
                  f'{contact.get("phone"):<20}'
                  f'{contact.get("comment"):<20}')
        print('=' * 63 + '\n')
    else:
        print(message)


def new_contact() -> dict:
    print()
    name = input(txt.new_name)
    phone = input(txt.new_phone)
    comment = input(txt.new_comment)
    print()
    return {'name': name, 'phone': phone, 'comment': comment}


def chose_to_del():
    while True:
        num_to_del = input(txt.choice_to_delete)
        if num_to_del.isdigit() and 0 < int(num_to_del) <= len(module.phone_book):
            return int(num_to_del) - 1
        else:
            print()
            print(txt.notnumber)


def confirm_func(message: str) -> bool:
    print()
    answer = input(message + ' (y/n) -> ')
    if answer.lower() == 'y':
        return True
    else:
        return False
