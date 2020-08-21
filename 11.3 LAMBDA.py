compras = (
    {'quantidade': 2, 'preço': 10},
    {'quantidade': 3, 'preço': 20},
    {'quantidade': 4, 'preço': 30},
    {'quantidade': 5, 'preço': 14},
)

totais = tuple(
    map(lambda compra: compra['quantidade'] * compra['preço'], compras)
)

print('Preços totais: R$', list(totais))
print('Total geral: R$ {:.2f}'.format(sum(totais)))
