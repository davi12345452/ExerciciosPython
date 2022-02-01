# Programa que define uma função que faz uma ficha do jogador
# e número de gols


def ficha(jog, gols):
    print("-"*20)
    print(f"Nome: {jog}\n"
          f"N° de gols: {gols}")
    print("-" * 20)


while True:
    n = str(input("Nome do jogador: "))
    g = int(input("Número de gols: "))
    ficha(n, g)
    while True:
        resposta = str(input("Deseja continuar cadastrando?[S/N] ")).upper()
        if resposta in "SN":
            break
        print("ERRO, digite sua resposta novamente")
    if resposta == "N":
        break

