# Programa que recebe como entrada um número , através do random,
# devolve como saída se o usuário acertou ou não

from random import randint as rd

print("O computador escolheu um número de 0 a 10, tenta adivinhá-lo")
n_comp = rd(0, 10)

n_usua = int(input("O seu palpite: "))
tentativas = 1

while n_comp != n_usua:
    tentativas += 1
    if n_comp > n_usua:
        print("Mais... Tente mais uma vez")
    else:
        print("Menos... Tente mais uma vez")
    n_usua = int(input("O seu palpite: "))

print(f"Parabens, você acertou o número com {tentativas} tentativas")