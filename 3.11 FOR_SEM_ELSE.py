PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')
TEXTOS = {'João gosta de futebol e política',
          'A praia foi divertida'
          }

for TEXTO in TEXTOS:
    found = False
    for palavra in TEXTO.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('O texto possui pelo menos uma palavra proibida,', palavra)
            found = True
            break

    if not found:
        print('Texto autorizado: ', TEXTO)