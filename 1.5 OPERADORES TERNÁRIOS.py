pergunta = str(input('Hoje está chuvendo(sim / não)? ')).upper()

if pergunta == 'SIM' or 'S' or 'YES' or 'Y':
    print('Hoje estou com as roupas molhadas.')
else:
    print('Hoje estou com as roupas secas.')