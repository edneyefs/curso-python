def faixa_etaria(idade):
    if 0 <= idade < 18:
        return 'MENOR DE IDADE'
    elif idade in range(18, 64):
        return 'ADULTO'
    elif idade in range(65, 100):
        return 'MELHOR IDADE'
    elif idade >= 100:
        return 'CENTENÁRIO'
    else:
        return '\033[31mIDADE INVÁLIDA\033[m'

if __name__ == '__main__':
    for idade in (17, 35, 87, 113, -2):
        print(f'{idade}: {faixa_etaria(idade)}')
