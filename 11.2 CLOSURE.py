def mutiplier(times):
    def calc(x):
        return x * times
    return calc


if __name__ == '__main__':
    dobro = mutiplier(2)
    triplo = mutiplier(3)

    print(dobro)
    print(triplo)

    print(f'O triplo de 3 é {triplo(3)}')
    print(f'O dobro de 7 é {dobro(7)}')
    print(f'O triplo de 3 é {triplo(3)}')
