'''
Найдите информацию об организациях.
a. Получите список ИНН из файла traders.txt.
b. Найдите информацию об организациях с этими ИНН в файле
traders.json.
c. Сохраните информацию об ИНН, ОГРН и адресе организаций из файла
traders.txt в файл traders.csv.

'''

import json
import csv
Koko = open('traders.txt', 'r')
innlist = Koko.readlines()
Koko.close()
rows = []
traders = open('traders.json', 'r')
traderslist = json.load(traders)
for i in innlist:
    a = i.rstrip('\n')
    for m in traderslist:
        if m['inn'] == a:
            rows.append([m['inn'],m['ogrn'],m['address'].replace(',', ' ')])
with open('traders.csv', 'w', newline='') as csvfile:     
    csvwriter = csv.writer(csvfile, delimiter=';')    
    csvwriter.writerows(rows)
