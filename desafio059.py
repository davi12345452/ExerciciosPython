# Programa que recebe como entrada 2 números, devolvendo como
# saída uma operação, escolhida pelo usuário, entre os números

num_1 = float(input("Primeiro número: "))
num_2 = float(input("Primeiro número: "))

while True:
    print("[1] - Soma \n"
          "[2] - Multiplicação \n"
          "[3] - Maior \n"
          "[4] - Novos Números\n"
          "[5] - Sair do Programa\n")
    opcao = int(input("Qual a sua opção:"))
    if opcao == 1:
        print(f"O resultado de {num_1} + {num_2} é {num_1 + num_2}")
    elif opcao == 2:
        print(f"O resultado de {num_1} x {num_2} é {num_1 * num_2}")
    elif opcao == 3:
        if num_1 > num_2:
            print(f"O número {num_1} é MAIOR que o número {num_2}")
        elif num_1 < num_2:
            print(f"O número {num_2} é MAIOR que o número {num_1}")
        else:
            print(f"Os números {num_1} e {num_2} são IGUAIS")
    elif opcao == 4:
        num_1 = float(input("Primeiro número: "))
        num_2 = float(input("Primeiro número: "))
    elif opcao == 5:
        break
    else:
        print("Erro, digite novamente")