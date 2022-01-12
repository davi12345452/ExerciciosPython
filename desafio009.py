# O programa recebe como entrada um número
# e devolve como saída a sua tabuada

numero = float(input("Digite um número para ver a sua tabuada: "))

contador = 1

# Contador para manipular o laço de repetição

print("--------------------")

while contador != 11:
    print(f"{numero} X {contador} = {numero * contador}")
    contador += 1

print("--------------------")