# Programa recebe de entrada um valor, devolvendo de saída
# esse valor de sequências de mega sena, por exemplo, se for
# 5 o valor, o programa devolvera 5 sorteios de mega

from random import randint

print("-"*50)
print("{:^50}".format("JOGO DE MEGA SENA"))
print("-"*50)

jogos = int(input("Quantos jogos você quer que eu sorteie? "))

for jogo in range(jogos):
    novo_jogo = []
    for count in range(6):
        num = randint(1, 60)
        novo_jogo.append(num)
    print(f"Jogo {jogo}: ", novo_jogo)