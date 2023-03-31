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
                    index = view.input_index('Введите номер изменяемого контакта: ')
                    while True:
                        if 0 < int(index) <= len(pb):
                            contact = view.change_contact(pb, index)
                            model.change_contact(contact, index)
                            view.show_message(
                                f'Контакт {model.get_phone_book()[index - 1].get("name")} успешно изменен!')
                            break

                        else:
                            print(f"Вы выбираете несуществующий контакт, введите от 1 до {len(pb)}")
                            index = view.input_index("Выберите номер изменяемого контакта: ")


            case 6:
                if view.show_contacts(pb, "Телефонная книга пуста или не открыта "):
                    index = view.input_index("Введите номер удаляемого контакта ")
                    while True:
                        if 0 < int(index) <= len(pb):
                            del_contact = model.delete_contact(index)
                            view.show_message(f"Контакт {del_contact} успешно удален!")
                            break

                        else:
                            print(f"Вы выбираете несуществующий контакт, введите от 1 до {len(pb)}")
                            index = view.input_index("Выберите номер удаляемого контакта: ")


            case 7:
                search = view.input_search("Введите искомый объект: ")
                result = model.find_contact(search)
                view.show_contacts(result, "Контакта не найдено")
            case 8:
                return
            case _:
                print("Invalid")

