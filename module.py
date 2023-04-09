import text_fields
import view

phone_book = []
start_phone_book = []
PATH = 'phone_book.txt'


def get_pb():
    return phone_book


def load_file():
    global start_phone_book
    with open(PATH, 'r', encoding='utf-8') as file:
        content = file.readlines()
    for contact in content:
        contact = contact.strip().split(';')
        phone_book.append({'name': contact[0], 'phone': contact[1], 'comment': contact[2]})
    start_phone_book = phone_book.copy()



def save_file():
    data = []
    for contact in phone_book:
        data.append(';'.join([value for value in contact.values()]))
    data = '\n'.join(data)
    with open(PATH, 'w', encoding='utf-8') as file:
        file.write(data)


def add_contact(contact: dict):
    phone_book.append(contact)


def find_contact(contact_to_find):
    index_list = []
    find_list = []
    with open(PATH, 'r', encoding='utf-8') as file:
        content = file.readlines()
        for k in range(len(content)):
            for elem in content[k].lower().strip().split(';'):
                if contact_to_find.lower() in elem:
                    index_list.append(k)
        for j in range(len(index_list)):
            find_list.append(content[index_list[j]].replace(";", ",    "))
        if len(find_list) == 0:
            view.print_info(text_fields.no_contact)
        else:
            print(*find_list)


def change_contact(num):
    new_name = input(text_fields.namechang)
    new_phone = input(text_fields.phonechang)
    new_comment = input(text_fields.comentchang)
    if new_name != '':
        phone_book[num]['name'] = new_name
    if new_phone != '':
        phone_book[num]['phone'] = new_phone
    if new_comment != '':
        phone_book[num]['comment'] = new_comment



def delete_contact(num_to_del):
    del phone_book[num_to_del]


def exit_pb() -> bool:
    if phone_book == start_phone_book:
        return False
    else:
        return True
