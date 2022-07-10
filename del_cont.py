import csv


def read_book():
    list_of_contacts = []
    with open ('phone_book.csv', 'r', newline='', encoding='utf-8') as book:
        reader = csv.DictReader(book, delimiter=';')
        counter = 0 
        for row in reader:
            counter += 1
            print(f'{counter}. {row["Фамилия"]} {row["Имя"]} {row["Телефон"]} {row["Описание"]}')
            list_of_contacts.append(row)

    return list_of_contacts
   

def delete_contact():
    list_of_contacts = read_book()

    contact_to_delete = input('Какой контакт удалить (введите номер): ')

    if contact_to_delete.isdigit() and 0 < int(contact_to_delete) <= len(list_of_contacts):
        contact_to_delete = list_of_contacts.pop(int(contact_to_delete) - 1)
    with open ('phone_book.csv', 'w', encoding='utf-8') as book:
        writer = csv.DictWriter(book, delimiter = ';', lineterminator="\r", fieldnames = list_of_contacts[0].keys())
        writer.writeheader()
        for i in list_of_contacts:
            writer.writerow(i)
    print(f'Контакт удален')

