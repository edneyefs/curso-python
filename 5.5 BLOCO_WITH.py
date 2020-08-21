# leitura stream v.5

with open('ARQUIVOS_CSV.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(registro.strip().split(',')))

if arquivo.closed:
    print('Arquivo fechado!')