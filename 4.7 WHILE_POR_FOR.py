print('\033[33mSEQUENCIA DE FIBONACCI v.8\033[m')

quantidade = int(input('Quantos números desejas mostrar da sequência? '))

def fibonacci(quantidade):
    resultado = [0, 1]
    for i in range (2, quantidade):
    # for i in range(quantidade - 2):
        resultado.append(sum(resultado[-2:]))
    return resultado

if __name__ == '__main__':
    for fib in fibonacci(quantidade):
        print(fib, end=' ')
