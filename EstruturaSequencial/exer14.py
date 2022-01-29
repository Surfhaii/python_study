peso = int(input("Quantos Kilos de peixe João trouxe hoje? "))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4.00

    print(f"João pescou um total de {peso:.2f} Kilos")
    print(f"João apresentou um excesso de {excesso:.2f} Kilos")
    print(f"João terá que pagar {multa:.2f} reais de multa")
else:
    print(f"João pescou um total de {peso:.2f} Kilos")
    print("Não precisará pagar multa")
