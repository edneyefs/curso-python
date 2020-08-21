# DESAFIO LEITURA CSV

import csv

with open('ibge.csv') as entrada:
    print('\033[31mBaixando o arquivo...\033[m')
    dados = entrada.read()
    for cidade in csv.reader(dados.splitlines()):
        print(f'{cidade[8]} : {cidade[3]}')
    print('\033[31mFIM\033[')