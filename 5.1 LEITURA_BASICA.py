# leitura v.1
arquivo = open('ARQUIVOS_CSV.csv')
dados = arquivo.read()
arquivo.close()
for registro in dados.splitlines():
    print('Nome:{}, Idade: {}'.format(*registro.split(',')))
