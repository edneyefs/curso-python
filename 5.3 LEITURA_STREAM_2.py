# leitura stream v.3
arquivo = open('ARQUIVOS_CSV.csv')
for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

arquivo.close()
