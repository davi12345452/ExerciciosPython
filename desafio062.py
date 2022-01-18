# Programa que recebe o primeiro termo e uma razão, devolvendo como saída
# uma Progressão Aritmética. A diferença com o exercício anterior, porém,
# é que o usário escolhe quantos termos pode ver

print("Gerador de PA\n"
      "=-=-=-=-=-=-=-=")

p_1 = float(input("Primeiro termo: "))
razao = float(input("Razão: "))
termo = 0

for count in range(10):
    termo = p_1 + (razao * count)
    print(termo, end = " -> ")

print("PAUSA")

mais = int(input("Quants termos você quer mostrar mais?"))

for count in range(10, (10 + mais), 1):
    termo = p_1 + (razao * count)
    print(termo, end = " -> ")

print("FIM")