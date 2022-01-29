notas = []
bimestre = 1
for contagem in range(4):
    nota = float(input("Qual é a nota do "+str(bimestre)+"º bimestre:"))
    notas.append(nota)
    bimestre+=1
media = (notas[0] + notas[1] + notas[2] + notas[3])/4
print("A média é: ", media)

#Tentando aplicar com list comprehension o exemplo acima
print("------------------")
lista = [float(input("Qual é a nota do bimestre:")) for contagem in range(4)]
media = (lista[0]+lista[1]+lista[2]+lista[3])/4
print("A Média é ", media)