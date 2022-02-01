class Salario:

    def __init__(self, salario=None, liquido=None, inss=0.08, ir=0.11, sindicato=0.05):
        self.salario = salario
        self.liquido = liquido
        self.inss = inss
        self.ir = ir
        self.sindicato = sindicato

    def calc_salario(self, recebe, horas):
        self.salario = recebe * horas
        self.inss = self.salario * self.inss
        self.ir = self.salario * self.ir
        self.sindicato = self.salario * self.sindicato
        self.liquido = self.salario - self.inss - self.sindicato - self.ir


horas = int(input("Quantas horas voce trabalhou esse mes ?"))
ganho = int(input("Quantos reais voce ganha por hora ?"))
p1 = Salario()
p1.calc_salario(ganho, horas)
print(f"+ Salário Bruto : R$ {p1.salario}")
print(f"- IR (11%) : R$ {p1.ir}")
print(f"- INSS (8%) : R$ {p1.inss}")
print(f"- Sindicato ( 5%) : R$ {p1.sindicato}")
print(f"= Salário Liquido : R$ {p1.liquido}")
print("bye")





