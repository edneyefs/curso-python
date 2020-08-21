# OPERADORES LÓGICOS
True or False
print(7 != 3 and 2 > 3)

# TABELA VERDADE DO AND
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# TABELA VERDADE DO OR
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# TABELA VERDADE DO XOR (OR EXCLUSIVE)
print(True != True)
print(True != False)
print(False != True)
print(False != False)

# OPERADOR DE NEGAÇÃO (UNÁRIO)
print(not True)
print(not False)

print(not 0)
print(not 1)
print(not -1)
print(not not True)

# CUIDADO
# OPERADORES BIT&BIT
print(True & False)
print(False or True)
print(True ^ False)

# AND BIT-A-BIT
#3 = 11
#2 = 10
print(3 & 2)

# OR BIT-A-BIT
#3 = 11
#2 = 10
print(3 or 2)

# XOR BIT-A-BIT
#3 = 11
#2 = 10
print(3 ^ 2)

saldo = 1000
salário = 4000
despesas = 2967

saldo_positivo = saldo > 0
despesas_controladas = salário - despesas >= 0.2 * salário
meta = saldo_positivo and despesas_controladas
#meta = saldo > 0 and salário - despesas >= 0.2 * salário
print(meta)
