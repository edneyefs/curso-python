#while True:
#    print('Vai demorar muito')

from random import randint

print('\033[34m*\033[m'*44)
print('ESTOU PENSANDO EM UM NÚMERO ENTRE 0 E 9...')
print('ADIVINHE...')
print('\033[34m*\033[m'*44)


número_informado = -1
número_secreto = randint(0,9)

while número_informado != número_secreto:
    número_informado = int(input('Informe o número: '))

print('Parabéns!!! O número era o {}'.format(número_secreto))
