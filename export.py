def export_data(data):
    with open('phone_book.csv', 'r+', encoding='utf-8') as file:
        contact = [line.strip('\n') for line in file]
        if data == True:
            for i in contact:
                for j in i.split(';'):
                    print(j)
                print()
        else:
            for i in contact:
                g = i
                if i[0] == ';':
                    g = i.replace(';', '', 1)
                print(g)
                print()

export_data(True)