def export_data(data):
    with open('phone_book.csv', 'r+', encoding='utf-8') as file, open('file_export.txt', 'w', encoding='utf-8',newline='') as file_ex:
        contact = [line.strip('\n') for line in file]
        count = 0
        if data == True:
            for i in contact:
                if len(i.split(';')) == 4:
                    for j in i.split(';'):
                        file_ex.write(f'{j}\n')
                    file_ex.write('\n')
                else:
                    if count == 4:
                        count = 0
                    if count != 4:
                        file_ex.write(f'{i}\n')
                        count += 1
        else:
            for i in contact:
                if len(i.split(';')) == 4:
                    file_ex.write(f'{i}' + '\n')

                else:
                    if count == 4:
                        file_ex.write('\n')
                        count = 0
                    elif count != 4:
                        file_ex.write(f'{i}')
                        count += 1
export_data(False)