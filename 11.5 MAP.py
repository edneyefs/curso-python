lista1 = [1, 2, 3]
dobro = map(lambda x: x *2, lista1)

print(list(dobro))

lista2 = [
    {'nome': 'João', 'idade': 31},
    {'nome': 'Maria', 'idade': 37},
    {'nome': 'José', 'idade': 26}
]

so_nomes = map(lambda nome: nome['nome'], lista2)
print(list(so_nomes))
so_idades = map(lambda idade: idade['idade'], lista2)
print(list(so_idades))

# Desafio usando map retorne frases '<Nome> tem <idade> anos.'

frases = map(lambda p: '{} tem {} anos'.format(p['nome'], p['idade']), lista2)
print(list(frases))
