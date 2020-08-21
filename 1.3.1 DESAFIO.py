# DESAFIO
trabalho_terça = True
trabalho_quinta = False
'''
Se os dois trabalhos True = Tv 50' + sorvete
Se um dos trabalhos True = Tv 32' + sorvete
Se os dois trabalhos False = Ficar em casa
'''
tv_50 = trabalho_terça and trabalho_quinta
sorvete = trabalho_terça or trabalho_quinta
tv_32 = trabalho_terça != trabalho_quinta
mais_saudavel = not sorvete

print('Tv 50pl {}\nTv 32pl {}\nSorvete {}\nFicar em casa {}'.format(tv_50, tv_32, sorvete, mais_saudavel))
