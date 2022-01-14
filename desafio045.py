# Programa Pedra, Papel ou Tesoura: recebe de entrada um número(escolha)
# devolvendo de saída se o jogador ou computador ganhou

from random import randint
from time import sleep

print("SUAS OPÇÕES:\n"
      "[0] - Pedra\n"
      "[1] - Papel\n"
      "[2] - Tesoura")

while True:
    escolha = int(input("A sua jogada: "))
    if 0 <= escolha <= 2:
        break

lista = ["Pedra", "Papel", "Tesoura"]

computador = randint(0, 2)

print("JO")
sleep(0.5)
print("KEN")
sleep(0.5)
print("PO!!!")
sleep(0.5)

print("==" * 10)
print("O jogador jogou {}".format(lista[escolha]))
print("O computador jogou {}".format(lista[computador]))
print("==" * 10)

if escolha == 0:
    if computador == 1:
        print("COMPUTADOR GANHOU")
    elif computador == 2:
        print("JOGADOR GANHOU")
if escolha == 1:
    if computador == 0:
        print("JOGADOR GANHOU")
    elif computador == 2:
        print("COMPUTADOR GANHOU")
if escolha == 2:
    if computador == 0:
        print("COMPUTADOR GANHOU")
    elif computador == 1:
        print("JOGADOR GANHOU")
else:
    print("EMPATE")