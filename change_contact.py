import csv
from del_cont import read_book
from add_contact import add_contact


def change_contact():

    list_of_contacts = read_book()

    contact_to_be_changed = input('Какой контакт вы хотите изменить (введите номер): ')

    new_data = add_contact()

    if contact_to_be_changed.isdigit() and 0 < int(contact_to_be_changed) <= len(list_of_contacts):
        contact_to_be_changed = list_of_contacts[int(contact_to_be_changed) - 1]

        contact_to_be_changed["Фамилия"] = new_data["Фамилия"]
        contact_to_be_changed["Имя"] = new_data["Имя"]
        contact_to_be_changed["Телефон"] = new_data["Телефон"]
        contact_to_be_changed["Описание"] = new_data["Описание"]

        # row["Фамилия"]} {row["Имя"]} {row["Телефон"]} {row["Описание"]

    with open ('phone_book.csv', 'w', encoding='utf-8') as book:
        writer = csv.DictWriter(book, delimiter=';', lineterminator="\r", fieldnames=list_of_contacts[0].keys())
        writer.writeheader()
        for i in list_of_contacts:
            writer.writerow(i)

    print(f'Контакт изменён')
