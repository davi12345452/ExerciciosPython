# Programa Par ou Ímpar, recebe como entrada um número
# e determina se é par ou ímpar

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número {} é PAR".format(numero))
else:
    print("O número {} é ÍMPAR".format(numero))