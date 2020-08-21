lista = []
print(type(lista))
print(dir(lista))
print(help(lista))
print(len(lista))#contador
lista.append(1)
lista.append(5)
print(len(lista))

nova_lista = [1, 4, 'Ana', 'Bia']
#print(nova_lista)
nova_lista.remove(4)
#print(nova_lista)
nova_lista.reverse()
print(nova_lista)

lista = [1, 5, 'Rebeca', 'Guilherme', 3.1415]
print(lista.index(1))
print(lista[2])
print(lista[-1])

lista = ['Ana', 'Lia', 'Rui', 'Paulo', 'Dani']
print(lista[1:3])
print(lista[1:-1])
print(lista[1:])
print(lista[::2])
print(lista[::-1])
del lista[2]
print(lista)
del lista[1:]
print(lista)
