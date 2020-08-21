from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

# português do Brasil
setlocale(LC_ALL, 'pt_BR')
# Listar todos os meses do ano com 31 dias
# 1. (filter) pegar o indice dos meses com 31 dias
meses_31 = filter(lambda mes: mdays[mes] == 31, range(1, 13))
# 2. (map) transformar os indices em nomes
nome_meses = map(lambda mes: month_name[mes], meses_31)
# 3. (reduce)juntar tudo para imprimir
juntar_meses = reduce(lambda todos, nome_mes: f'{todos}\n- {nome_mes}', nome_meses, 'Meses com 31 dias:')

print(juntar_meses)
