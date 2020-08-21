PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'política'}
TEXTOS = {'João gosta de futebol e política',
          'A praia foi divertida'
          }
for texto in TEXTOS:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print('Foi encontrado pelo menos uma palavra proibida, ', intersecao)
    else:
        print('Texto autorizado:', texto)
