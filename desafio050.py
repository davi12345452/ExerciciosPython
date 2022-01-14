# Programa que recebe como entrada a entrada de 6 números, devolvendo
# como saída somente a soma dos pares

lista = []
soma = 0

for cont in range(1, 7):
    num = float(input("Digite o {}° valor: ".format(cont)))
    lista.append(num)

for cont in range(6):
    if lista[cont] % 2 == 0:
        soma += lista[cont]

print("\nA soma dos pares é igual a {}".format(soma))
