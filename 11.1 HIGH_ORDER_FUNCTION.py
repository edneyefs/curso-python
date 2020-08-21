def dobro(x):
    return x * 2


def quadrado(x):
    return x ** 2


def process(titulo, lista, funcao):
    print(f'Processando: {titulo}')
    for i in lista:
        print(i, '=>', funcao(i))


if __name__ == '__main__':
    process('Dobros de 1 a 10', range(1, 11), dobro)
    process('Quadrado de 1 a 10', range(1, 11), quadrado)
