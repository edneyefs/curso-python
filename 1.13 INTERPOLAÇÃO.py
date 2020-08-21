from string import Template

nome, idade = 'Ana', 30.9875
print('Nome: %s Idade: %.2f, %s %s' % (nome, idade, True, False))
print('Nome: {0} Idade: {1}'.format(nome, idade))
print(f'Nome: {nome} Idade: {idade}')

s = Template('Nome: $nome Idade: $idade')
print(s.substitute(nome = nome, idade = idade))
