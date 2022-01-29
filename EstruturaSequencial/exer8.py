print("Programa para ver quanto eu ganho no mes")

salario = float(input("Quanto voce ganha por hora: "))
horas = int(input("Quantas horas foram trabalhadas nesse mes: "))

pagamento = salario*horas

print("Seu salário é {:.2f} reais".format(pagamento))