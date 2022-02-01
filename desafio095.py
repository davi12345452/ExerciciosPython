# Programa que recebe de entrada jogadores, e seus gols por partidas
# devolvendo uma tabela de análise e manipulação pelo usuário como
# saída

lista_jogadores = list()
jogador = dict()

while True:
    jogador.clear()
    jogador["nome"] = str(input("Nome do jogador: "))
    partidas = int(input("Número de partidas: "))
    gols = list()
    for partida in range(partidas):
        gol = int(input(f"\tQuantos gols na partida {partida+1}? "))
        gols.append(gol)
    jogador["gols"] = gols
    jogador["total"] = sum(gols)
    while True:
        resposta = str(input("Deseja continuar cadastrando?[S/N] ")).upper()
        if resposta in "SN":
            break
        print("ERRO, digite sua resposta novamente")
    lista_jogadores.append(jogador.copy())
    if resposta == "N":
        break

print("-="*25)
print("%-4s%-15s%-15s%-6s" % ("Cod", "Nome", "Gols", "Total"))
print("-"*40)
cont = 0
for elem in lista_jogadores:
    print("%-4d%-15s%-15s%-6d" % (cont, elem["nome"], str(elem["gols"]), elem["total"]))
    cont += 1
print("-"*40)

while True:
    resposta = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if resposta == 999:
        break
    try:
        print(f"LEVANTAMENTO DO JOGADOR {lista_jogadores[resposta]['nome']}")
        cont = 1
        for elem in lista_jogadores[resposta]["gols"]:
            print(f"\tNo jogo {cont} fez {elem} gols.")
            cont += 1
    except:
        print(f"ERRO, não existe jogador com código {resposta}")

print("-"*40)
print("ENCERRADO")

