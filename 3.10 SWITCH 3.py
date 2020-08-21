def get_tipo_dia(dia):
    dias = {1: '\033[31mFINAL DE SEMANA\033[m',
            2: '\033[34mDIA DE SEMANA\033[m',
            3: '\033[34mDIA DE SEMANA\033[m',
            4: '\033[34mDIA DE SEMANA\033[m',
            5: '\033[34mDIA DE SEMANA\033[m',
            6: '\033[34mDIA DE SEMANA\033[m',
            7: '\033[31mFINAL DE SEMANA\033[m'
            }
    return dias.get(dia, '**\033[31mINVÁLIDO\33[m**')
def get_dias_semana(dia):
    dias = {1: 'DOMINGO',
            2: 'SEGUNDA',
            3: 'TERÇA',
            4: 'QUARTA',
            5: 'QUINTA',
            6: 'SEXTA',
            7: 'SÁBADO',
            }
    return dias.get(dia, '**\033[31mINVÁLIDO\33[m**')
if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia}: {get_dias_semana(dia)} - {get_tipo_dia(dia)}')