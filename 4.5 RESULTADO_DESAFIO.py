print('\033[33mSEQUENCIA DE FIBONACCI v.6\033[m')

limite = int(input('Quantos número limite da sequência você quer mostrar? '))

def fibonacci(limite):
    resultado = [0, 1]
    while resultado[-1] < limite:
        resultado.append(sum(resultado[-2:]))
    return resultado

if __name__ == '__main__':
    for fib in fibonacci(limite):
        print(fib, end=', ')
