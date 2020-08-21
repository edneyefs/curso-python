class Data:
    def __init__(self, dia=1, mes=1, ano=1970):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):#to_str(self):
        return f'{self.dia}/{self.mes}/{self.ano}'

d1 = Data(5, 12, 2019)
# d1.dia = 5
# d1.mes = 12
# d1.ano = 2019
print(d1)#.to_str()

d2 = Data(ano=2022, mes=12)
d2.dia = 12
# d2.mes = 11
# d2.ano = 2021
print(d2)#.to_str()
