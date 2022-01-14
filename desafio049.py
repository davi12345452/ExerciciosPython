# Programa recebe de entrada um número, devolvendo
# como saída a sua tabuada

numero = float(input("\nDigite o número que deseja ver a tabuada: "))

for cont in range(1, 11):
    print("{} -> ".format(numero * cont), end="")

print("ACABOU")
