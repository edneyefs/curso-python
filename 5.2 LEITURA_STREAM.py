# leitura stream v.2
arquivo = open('ARQUIVOS_CSV.csv')
for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))
arquivo.close()
