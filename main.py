from menu import menu
from add_contact import save_contact, add_contact, header
from export import export_data
from import_cont import import_data
from del_cont import delete_contact

def phone_book():
    user_input = 'random'
    while True:
        menu()
        user_input = input('Какое действие выполнить (введите номер)? ')
        if user_input == '1':
            save_contact(add_contact())
        elif user_input == '2':
            pass
        elif user_input == '3':
            export_data()
        elif user_input == '4':
            import_data()
        elif user_input == '5':
            delete_contact()

phone_book()



