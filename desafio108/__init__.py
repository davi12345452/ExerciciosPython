# Arquivo de teste para uso das funções do exercício 108, para que sejam usadas
# como módulo

import modulo as md

valor = float(input("Digite um valor: "))
print(f"A metade de {md.moeda(valor)} é {md.moeda(md.metade(valor))}.")
print(f"O dobro de {md.moeda(valor)} é {md.moeda(md.dobro(valor))}.")
print(f"Aumentando 10% de {md.moeda(valor)} temos {md.moeda(md.juros(True, 10, valor))}.")