import csv

def addContact():
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


#def header(data):
#    with open ('phone_book.csv', 'a', newline='', encoding='utf-8') as book:
#        writer = csv.writer(book, delimiter = ';')
#        writer.writerow(data.keys())

def saveContact(data):
    with open ('phone_book.csv', 'a', newline='', encoding='utf-8') as book:
        writer = csv.writer(book, delimiter=';')
        writer.writerow(data.values())


#header({'Фамилия': '', 'Имя': '', 'Телефон': '', 'Описание': '',})
for i in range (8):
    saveContact(addContact())








