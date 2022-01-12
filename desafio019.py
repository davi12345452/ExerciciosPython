# Programa recebe o nome de 4 alunos e devolve como saída
# o nome de um dos 4, de maneira aleatória, por causa da
# biblioteca random.

from random import randint

nome1 = str(input("Primeiro nome: "))
nome2 = str(input("Segundo nome: "))
nome3 = str(input("Terceiro nome: "))
nome4 = str(input("Quarto nome: "))

lista_de_nomes = [nome1, nome2, nome3, nome4]

nome_sorteado = lista_de_nomes[randint(0, 3)]

print("O nome sorteado foi: {}".format(nome_sorteado))