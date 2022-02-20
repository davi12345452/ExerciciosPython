# Programa que utiliza as mesmas funções que o desafio108, porém altera algumas coisas
# na página de teste

import modulo as md

valor = float(input("Digite um valor: "))
print(f"A metade de {md.moeda(valor)} é {md.metade(valor, True)}.")
print(f"O dobro de {md.moeda(valor)} é {md.dobro(valor, True)}.")
print(f"Aumentando 10% de {md.moeda(valor)} temos {md.juros(True, 10, valor, True)}.")