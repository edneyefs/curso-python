# leitura stream v.6

with open('ARQUIVOS_CSV.csv') as arquivo:
    with open('ARQUIVO_CSV.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa), file = saida)

if arquivo.closed:
    print('Arquivo fechado!')

if saida.closed:
    print('Arquivo de saida fechado!')
