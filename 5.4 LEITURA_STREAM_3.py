# leitura stream v.4

try:
    arquivo = open('ARQUIVOS_CSV.csv')

    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

except IndexError: #faz uma exceção para o prosseguimento do código
    pass #bloco em branco só para não dar error

finally:
    print('FIM')
    arquivo.close()

if arquivo.closed:
    print('Arquivo fechado!')