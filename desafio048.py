# Programa que calcula soma dos número ímpares e múltiplos de 3
# em um intervalo de 1 a 500

soma = 0
todos = 0

for cont in range(1, 501):
    if cont % 2 == 1 and cont % 3 == 0:
        soma += cont
        todos += 1

print("A soma de {} números é {}".format(todos, soma))