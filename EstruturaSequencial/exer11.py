a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))
c = int(input("Digite o terceiro número real: "))
print("------------------------------")

def letraA(a, b):
    dobro = a * a
    metade = b / 2
    produto = dobro * int(metade)
    print("Letra A: "+str(produto))

letraA(a, b)

def letraB(a, c):
    triplo = a*a*a
    soma = triplo + c
    print(f"Letra B: {soma}")

letraB(a, c)

def letraC(c):
    cubo = (c*c)*c
    print(f"Letra C: {cubo}")

letraC(c)