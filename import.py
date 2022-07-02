import csv

def import_data(data):
    with open('file_import.txt', 'r') as file_im, open('phone_book.csv', 'a') as pb:
        contact = [line.strip('\n') for line in file_im]
        count = 0
        if data == True:
            for i in contact:
                if len(i.split(';')) == 4:
                    for j in i.split(';'):
                        pb.write(f'{j}\n')
                    pb.write('\n')
                else:
                    if count == 4:
                        count = 0
                    if count != 4:
                        pb.write(f'{i}\n')
                        count += 1
        else:
            for i in contact:
                if len(i.split(';')) == 4:
                    pb.write(f'{i}' + '\n')
                else:
                    if count == 4:
                        pb.write('\n')
                        count = 0
                    elif count != 4:
                        pb.write(f'{i}')
                        count += 1

import_data(True)
                    