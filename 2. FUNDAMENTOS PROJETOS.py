from time import sleep
from math import pi

print('-'*22)
print('\033[32mÁREA DA CIRCUNFERÊNCIA V 1.0\033[m')
print('-'*22)

raio = input('Qual o valor do raio da circunferêcia? ')

def area_circunferencia(raio):
    return pi * float(raio) ** 2
def help():
    print('\033[31mCOMANDO INVÁLIDO!\033[m É necessário digitar um número válido. Ex: 12, 13.1, etc')

print('\33[34mCALCULANDO...\33[m')

sleep(2)

if float(raio) >= 0.1:
    print('O área da sua circunferência é de {:.2f} cm'.format(area_circunferencia(raio)))
else:
    print(help())