print('\033[33mSEQUENCIA DE FIBONACCI v.6\033[m')

quantidade = int(input('Quantos números da sequência você quer mostrar? '))

def fibonacci(quantidade):
    resultado = [0, 1]
    while True:
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == quantidade:
            break
    return resultado

if __name__ == '__main__':
    for fib in fibonacci(quantidade):
        print(fib, end=', ')
