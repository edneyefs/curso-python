def nota_conceito(valor):
    nota = float(valor)

    if nota > 10:
        return('\033[31mNota inválida\033[m')
    elif nota >= 9.1:
        return ('Conceito é A')
    elif nota >= 8.1:
        return ('Conceito é A-')
    elif nota >= 7.1:
        return ('Conceito é B')
    elif nota >= 6.1:
        return ('Conceito é B-')
    elif nota >= 5.1:
        return ('Conceito é C')
    elif nota >= 4.1:
        return ('Conceito é C-')
    elif nota >= 3.1:
        return ('Conceito é D')
    elif nota >= 2.1:
        return ('Conceito é D-')
    elif nota >= 1.1:
        return ('Conceito é E')
    elif nota == 0.0:
        return ('Conceito é E-')
    else:
        return ('\033[31mNota inválida\033[m')

if __name__ == '__main__':
    valor_informado = input('Nota do aluno: ')
    conceito = nota_conceito(valor_informado)
    print(conceito)