print('\033[33mSEQUENCIA DE FIBONACCI RECURSIVA v.1\033[m')

quantidade = int(input('Quantos números desejas mostrar da sequência? '))

def fibonacci(quatidade, sequencia = (0, 1)):
    # condição de parada
    return sequencia if len(sequencia) == quantidade else \
        fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))

if __name__ == '__main__':
    for fib in fibonacci(quantidade):
        print(fib, end=' ')
    print('\n\033[31mFIM!\033[m')
