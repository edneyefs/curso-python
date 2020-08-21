# leitura modo csv v.7

import csv
with open('ARQUIVOS_CSV.csv') as entrada:
    for pessoa in csv.reader(entrada):
        print('Nome: {}, Idade: {}'.format(*pessoa))

