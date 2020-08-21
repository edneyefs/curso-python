from time import sleep
from math import pi
import sys
import errno

class terminalcolor:
    erro = '\033[031m'
    apresentation = '\033[32m'
    normal = '\033[m'

print('-'*22)
print(apresentation + 'ÁREA DA CIRCUNFERÊNCIA V 1.0\033[m' + normal)
print('-'*22)

def area_circunferencia(raio):
    return pi * float(raio) ** 2

def help():
    print('\033[31mCOMANDO INVÁLIDO!\033[m É necessário digitar um número válido. Ex: 12, 13.1, etc')
    print('Sintaxe: {}'.format(sys.argv[0][2:1]))

    print('\33[34mCALCULANDO...\33[m')

    sleep(2)

    if __name__ == '__main__':
        if len(sys.argv) < 2:
            help()
            sys.exit(errno.EPERM)

        elif not sys.argv[1].isnumeric():
            help()
            print('\33[31mO raio deve ser um valor númerico\33[m')
            sys.exit(errno.EINVAL)

            raio = sys.argv[1]
            #area = area_circunferencia(raio)
            print('O área da sua circunferência é de {:.2f} cm'.format(area_circunferencia(raio)))
