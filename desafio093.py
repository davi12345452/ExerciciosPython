# Programa recebe de entrada dados sobre um jogador
# devolvendo como saída essas informações

jogador = dict()

jogador["nome"] = str(input("Nome do jogador: "))
partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

lista_gols = list()

for cont in range(partidas):
    gol = int(input(f"\tQuantos gols na partida {cont}? "))
    lista_gols.append(gol)

print("-="*20)

jogador["gols"] = lista_gols
jogador["total"] = sum(lista_gols)
print(jogador)

print("-="*20)

for chave, cont in jogador.items():
    print(f"O campo {chave} tem valor {cont}.")

print("-="*20)

cont = 0
print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas")
for partida in jogador["gols"]:
    print(f"=> Na partida {cont} fez {partida} gols")
    cont += 1
print(f"Foi um total de {jogador['total']} gols.")