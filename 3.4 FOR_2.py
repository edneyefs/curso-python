# STRING
palavra = 'paralelepipedo'
for letra in palavra:
    print(letra, end='')
    print('Fim')


# LISTA
aprovados = ['Rafaela', 'Pedro', 'Renato', 'Maria']
for nome in aprovados:
    print(nome)
for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1})', nome)

# TUPLA
dias_da_semana = ('Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado')
for dia in dias_da_semana:
    print(f'Hoje é {dia}')


# SET
for letra in set('Muito Legal'):
    print(letra)
