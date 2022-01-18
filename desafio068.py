# Programa Par ou Ímpar, usuário da de entrada um número e uma string(P OU I)
# recebendo como saída as jogados computador e quem ganhou.

from random import randint as rdt

print("-=" * 15)
print("JOGO DO PAR OU ÍMPAR")
print("-=" * 15)
vitorias = 0

while True:
    jogador = int(input("Diga um valor: "))
    p_ou_i = str(input("Par ou Ímpar? [P]/[I] ")).upper()
    print("--" * 15)
    computador = rdt(0, 10)
    total = jogador + computador
    resultado = ""
    if total % 2 == 0:
        print(f"Você jogou {jogador} e o computador {computador}. Total de {total} DEU PAR")
        resultado = "P"
    else:
        print(f"Você jogou {jogador} e o computador {computador}. Total de {total} DEU ÍMPAR")
        resultado = "I"
    print("--" * 15)
    if p_ou_i == resultado:
        print("Você VENCEU!")
        vitorias += 1
        print("Vamos jogar novamentes...")
        print("-=" * 15)
    else:
        print("Você PERDEU!")
        print("-=" * 15)
        break

print(f"GAME OVER. Você venceu {vitorias} vezes")