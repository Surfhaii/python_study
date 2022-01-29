print("Qual é o seu sexo? ")
print("[1] Masculino    [2] Feminino")
sexo = input("R:")
altura = float(input("Digite sua altura: "))

if sexo == '1':
    calculo = (72.7 * altura) - 58
    print(f"Seu peso ideal é {calculo:.2f}")
elif sexo == '2':
    calculo = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é {calculo:.2f}")
else:
    print("Sexo ou altura não especificado!")