import csv
import os

def add_contact():
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
    return phone_book


def header():
    with open ('phone_book.csv', 'w', newline='', encoding='utf-8') as book:
        header_names = ['Фамилия', 'Имя', 'Телефон', 'Описание']
        writer = csv.DictWriter(book, delimiter = ';',lineterminator = "\r", fieldnames = header_names)
        writer.writeheader()

def save_contact(data):
    with open ('phone_book.csv', 'a', newline='', encoding='utf-8') as book:
        writer = csv.writer(book, delimiter=';')
        if os.stat("phone_book.csv").st_size == 0:  #проверка файла на пустоту
            writer.writerow(data.keys())
        writer.writerow(data.values())
    print('Контакт сохранен')










