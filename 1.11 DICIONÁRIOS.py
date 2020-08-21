# NORMALMENTE SÃO STRINGS
pessoa = {'nome': 'Prof(a). Ana', 'idade': 38, 'cursos':['Inglês', 'Português']}
print(type(pessoa))
print(dir(pessoa))
print(len(pessoa))
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['cursos'][1])
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa.get('idade'))
print(pessoa.get('tags'))

pessoa = {'nome': 'Prof(o). Alberto', 'idade': 43, 'cursos': ['React', 'Python']}
pessoa['idade'] = 44
pessoa['cursos'].append('Angular')
pessoa.pop('idade')
pessoa.update({'idade': 40, 'Sexo': 'M'})
del pessoa['cursos']
print(pessoa)
print(pessoa.clear())
