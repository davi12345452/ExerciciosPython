# Jogo de adivinhação, computador escolhe um número aleatoriamente
# e o usuário deve dar de entrada um chute de qual é esse número

from random import randint

print("-=-"*15)
print("Vou pensar em um número de 1 a 5, tente adivinhar")
print("-=-"*15)

numero_c = randint(1, 5)
numero_p = int(input("\nTente adivinhar o número: "))

if numero_p == numero_c:
    print("Você acertou, parabéns!")
else:
    print("Você errou, que pena...")