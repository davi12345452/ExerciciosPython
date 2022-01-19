# Programa que não recebe entrada, apenas cria uma tupla com 5 valores aleatórios
# e devolve como saída essa tupla, o maior e menor termo

from random import randint

tupla = (randint(1, 10), randint(1, 10), randint(1, 10),
         randint(1, 10), randint(1, 10))

maior = 0
menor = 10

for num in tupla:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print("Os números sorteados foram: ", tupla)
print(f"Maior: {maior}\n"
      f"Menor: {menor}")