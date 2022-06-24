import csv

def table(data_1, data_2):
    with open(data_1, 'r+', encoding='utf-8') as pb, open(data_2, 'r+', encoding='utf-8') as sm:
        array = [row.strip() for row in pb]
        del array[0]
        for i in array:
            s = ''
            for j in i:
                if j == ';':
                    sm.write(f'{s};\n')
                    s = ''
                else:
                    s += j
            sm.write(f'{s};\n\n ')

table('phone_book.csv', 'sim.csv')

def stroka(data_1, data_2):
    with open(data_1, 'r+', encoding='utf-8') as pb, open(data_2, 'r+', encoding='utf-8') as sm:
        file = csv.reader(pb, delimiter='\n')
       

stroka('phone_book.csv', 'sim.csv')