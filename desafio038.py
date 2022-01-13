# Programa recebe de entrada 2 números, devolvendo como saída
# uma comparação entre eles, se são iguais ou qual é maior e menor

num_1 = float(input("Primeiro número: "))
num_2 = float(input("Segundo número: "))

if num_2 == num_1:
    print("Os dois números são IGUAIS.")
elif num_1 > num_2:
    print("O PRIMEIRO número é maior.")
else:
    print("O SEGUNDO número é maior.")