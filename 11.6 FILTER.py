from functools import reduce

pessoas = [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 17},
    {'nome': 'João', 'idade': 31},
    {'nome': 'Maria', 'idade': 37},
    {'nome': 'José', 'idade': 26},
]

menores = filter(lambda p: p['idade'] < 18, pessoas)
print(list(menores))
maiores = filter(lambda p: p['idade'] > 18, pessoas)
print(list(maiores))

# Desafio filtrar nome e retornar aqueles com mais de 6 caracteres
nome_grandes = filter(lambda p: len(p['nome']) >= 7, pessoas)
print(list(nome_grandes))
