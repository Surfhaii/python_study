from pessoa import Pessoa

# criar um hub de cadastro
cadastro = True

while cadastro:
    print("Digite [1] para realizar cadastro e [2] para sair.")
    escolha = input()
    if escolha == '1':
        decisao = True
    else:
        break

    if decisao:
        print("-----------------")
        print("Ficha de cadastro")
        print("-----------------")
        nome = str(input("Nome: "))
        idade = int(input("Idade: "))
        sexo = str(input("Sexo: "))
        p = Pessoa(nome, idade, sexo)
        cadastro = False

sair = 1
alternativas = True
acao = 1
while sair == 1:
    while alternativas:
        print("Escolha qual ação fazer:")
        print("[1] Comer  [2] parar de comer.")
        print("[3] Falar  [4] parar de falar.")
        print("[5] Andar  [6] parar de andar.")
        print("[7] dormir  [8] parar de dormir")
        alternativas = False
    while acao == 1:
        opcao = input("escolha: ")
        if opcao == '1':
            p.comer()
        elif opcao == '2':
            p.parar_comer()
        elif opcao == '3':
            p.falar()
        elif opcao == '4':
            p.parar_falar()
        elif opcao == '5':
            p.andar()
        elif opcao == '6':
            p.parar_andar()
        elif opcao == '7':
            p.dormir()
        elif opcao == '8':
            p.parar_dormir()
        print("deseja fazer outra ação?")
        print("[1] SIM [2] NÃO")
        acao = int(input())
    final = int(input("[1] Ver ações [2] Sair [3] escolher ação"))
    if final == 1:
        alternativas = True
    elif final == 2:
        sair = 0
    elif final == 3:
        acao = 1