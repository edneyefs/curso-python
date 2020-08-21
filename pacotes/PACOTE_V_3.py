from pacotes.pacote1 import modulo1
from pacotes.pacote2 import modulo1 as modulo1_sub


print(f'3 + 2 = {modulo1.soma(3, 2)}')
print(f'3 - 2 = {modulo1_sub.subtracao(3, 2)}')

print('\033[31mFIM!\033[m')
