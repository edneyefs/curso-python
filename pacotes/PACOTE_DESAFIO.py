from pacotes.app.utils.gerador import novo_nome
from pacotes.app.negocio import nome_existe
from pacotes.app.negocio.backend import add_nome

def main():
    while True:
        nome = novo_nome()
        if not nome_existe(nome):
            add_nome(nome)
            break
    print(f'Criado o novo nome de testes: {nome}')

if __name__ == '__main__':
    main()
