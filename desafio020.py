# Programa recebe de entrada 4 nomes, devolvendo como
# saída uma ordem aleatório com esses 4 nomes

import random
from time import sleep


nome1 = str(input("Primeiro nome: "))
nome2 = str(input("Segundo nome: "))
nome3 = str(input("Terceiro nome: "))
nome4 = str(input("Quarto nome: "))

lista_de_nomes = [nome1, nome2, nome3, nome4]

print("A ordem será sorteada em....")
print("3")
sleep(1)
print("2")
sleep(1)
print("1")
sleep(1)

random.shuffle(lista_de_nomes)

print(f"\n1° - {lista_de_nomes[0]}\n2° - {lista_de_nomes[1]}\n3° - {lista_de_nomes[2]}\n4° - {lista_de_nomes[3]}")
