# for i in range(1, 10):
#    if i == 6:
#        break
#    print(i)
# else:
#    print('FIM')


from random import randint

def sortear_dado():
    return randint(1, 6)
print(sortear_dado())

for número in range(1, 7):
    if número % 2 == 1:
        continue

    if sortear_dado() == número:
        print('ACERTOU!', número)
        break

else:
    print('Não acertou! :(')
