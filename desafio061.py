# Programa que recebe o primeiro termo e uma razão, devolvendo como saída
# uma Progressão Aritmética

print("Gerador de PA\n"
      "=-=-=-=-=-=-=-=")

p_1 = float(input("Primeiro termo: "))
razao = float(input("Razão: "))
termo = 0

for count in range(10):
    termo = p_1 + (razao * count)
    print(termo, end = " -> ")

print("FIM")