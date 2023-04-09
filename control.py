import view
import module
import text_fields


def start_pb():
    module.load_file()
    view.print_info(text_fields.load_successful)
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                module.save_file()
                view.print_info(text_fields.save_successful)

            case 2:
                pb = module.get_pb()
                view.show_contacts(pb, text_fields.no_contact_or_file)

            case 3:
                contact = view.new_contact()
                module.add_contact(contact)
                view.print_info(text_fields.new_contact_successful)

            case 4:
                print()
                contact_to_find = input(text_fields.find_contact)
                module.find_contact(contact_to_find)

            case 5:
                pb = module.get_pb()
                view.show_contacts(pb, text_fields.no_contact_or_file)

                num_to_change = view.num_to_find()
                module.change_contact(num_to_change)

                module.save_file()
                view.print_info(text_fields.save_successful)

            case 6:
                pb = module.get_pb()
                view.show_contacts(pb, text_fields.no_contact_or_file)
                num_to_del = view.chose_to_del()
                module.delete_contact(num_to_del)
                view.print_info(text_fields.delete_done)

            case 7:
                if module.exit_pb():
                    if view.confirm_func(text_fields.is_changed):
                        module.save_file()
                view.print_info(text_fields.exit_prog)
                exit()
