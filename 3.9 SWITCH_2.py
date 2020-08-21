def get_dia_semana(dia):
    dias = {1: 'DOMINGO',
            2: 'SEGUNDA',
            3: 'TERÇA',
            4: 'QUARTA',
            5: 'QUINTA',
            6: 'SEXTA',
            7: 'SÁBADO',
            }
    return dias.get(dia, '**\033[31minválido\033[m**')
if __name__ == '__main__':
    for dia in range(0, 9):
         if dia == 1 or dia == 7:
             print(f'{dia}: {get_dia_semana(dia)} \033[31mFINAL DE SEMANA\033[m', end='\n')
             continue
         if dia == 0 or dia == 8:
             print(f'{dia}: {get_dia_semana(dia)}')
             continue
         print(f'{dia}: {get_dia_semana(dia)} \33[34mSEMANA\33[m')
