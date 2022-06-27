import csv

def import_data(data):
    with open('phone_book.csv', 'a', encoding='utf-8') as pb:
        file_writer = csv.writer(pb, delimiter = ";", lineterminator="\r")
        if data == True:
            phone_book = {'Фамилия': '', 'Имя': '', 'Телефон': '', 'Описание': '',}
            for key in phone_book:
                phone_book[key] = input(f'{key.upper()}: ').capitalize()
                if key.lower() in ['фамилия', 'имя', 'описание']:
                    while len(phone_book[key]) > 32:
                        print("Значение превышает допустимый лимит")
                        phone_book[key] = input(f'{key.upper()}: ').capitalize()
                else:
                    while not phone_book['Телефон'].isdigit():
                        print ('Номер должен содержать только цифры')
                        phone_book[key] = input(f'{key}: ')
            writer = csv.writer(pb, delimiter=';')
            writer.writerow(phone_book.values())
        else:
            print("Фамилия: Имя: Телефон: Описание: ")
            contact = list(input('Заполните поля по указанной выше форме: ').split())
            file_writer.writerow(contact)

import_data(False)