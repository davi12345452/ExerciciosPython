# Programa que recebe um número e diz se ele é ou não
# primo como saída

numero = int(input("Digite um número: "))
div = 0

for cont in range(1, (numero + 1)):
    if numero % cont == 0:
        div += 1
        print("\033[33m{}".format(cont), end=" ")
    else:
        print("\033[31m{}".format(cont), end=" ")

if div <= 2:
    print("\n\n\033[mO número {} É PRIMO".format(numero))
else:
    print("\n\n\033[mO número {} NÃO É PRIMO, pois foi dividido\n{} vezes incluindo ele mesmo e 1.".format(numero, div))