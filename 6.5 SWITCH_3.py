def get_tipo_dia(dia):
    dias = {
        (1, 7): '\033[31mFINAL DE SEMANA\033[m',
        tuple(range(2,7)): '\033[34mDIA DE SEMANA\033[m',
    }
    dia_escolhido = (tipo for numeros, tipo in dias.items() if dia in numeros)
    return next(dia_escolhido, '** dia inválido **')

if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia}: {get_tipo_dia(dia)}')
