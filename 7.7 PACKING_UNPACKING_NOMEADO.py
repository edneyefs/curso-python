# **kwargs
# PACKING
def resultado_f1(**podium):
    for posição, piloto in podium.items():
        print(f'{posição} -> {piloto}')

if __name__ == '__main__':
    resultado_f1(primeiro='L. Hamilton',
                 segundo='M. Verstappen',
                 terceiro='S.Vettel')

# UNPACKING
def resultado_f1(primeiro, segundo, terceiro):
    print(f'1) {primeiro}')
    print(f'2) {segundo}')
    print(f'3) {terceiro}')

if __name__ == '__main__':
    podium = {'segundo': 'M. Verstappen',
              'primeiro': 'L. Hamilton',
              'terceiro': 'S. Vettel'}
    resultado_f1(**podium)