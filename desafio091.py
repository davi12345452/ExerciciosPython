# Programa que não recebe entrada, apenas simula um jogo de dados
# com 4 jogadores utilizando dicionário para armazenar as informações

from random import randint
from operator import  itemgetter

jogadas = {"jogador1" : randint(1, 6),
           "jogador2" : randint(1, 6),
           "jogador3" : randint(1, 6),
           "jogador4" : randint(1, 6)}

for jogador, jogada in jogadas.items():
    print(f"O {jogador} jogou {jogada}.")

rank = sorted(jogadas.items(), key=itemgetter(1), reverse=True)

print("")
for posicao, jogador in enumerate(rank):
    print(f"{posicao + 1}° lugar: {jogador[0]}")



