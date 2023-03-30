import model
import view

def start ():
    while True:
        pb = model.get_phone_book()
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file()
                view.show_message("Файл открыт")
            case 2:
                model.save_phone_book()
                view.show_message("Файл сохранен")
            case 3:
                view.show_contacts(pb, "Телефонная книга пуста или не открыта")
            case 4:
                contact = view.add_contact()
                model.add_contact(contact)
            case 5:
                if view.show_contacts(pb, 'Телефоннаф книга пуста или не открыта'):
                    index = view.input_index('Введите номер изменяемого контакта ')
                    contact = view.change_contact(pb, index)
                    model.change_contact(contact, index)
                    view.show_message(f'Контакт {model.get_phone_book()[index - 1].get("name")} успешно изменен!')

            case 6:
                if view.show_contacts(pb, "Телефонная книга пуста или не открыта "):
                    index = view.input_index("Введите номер удаляемого контакта ")
                    del_contact = model.delete_contact(index)
                    view.show_message(f"Контакт {del_contact} успешно удален!")

            case 7:
                search = view.input_search("Введите искомый объект: ")
                result = model.find_contact(search)
                view.show_contacts(result, "Контакта не найдено")
            case 8:
                return
            case _:
                print("Invalid")

