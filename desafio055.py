# Programa recebe de entrada o peso de 5 pessoas, devolvendo
# como saída o maior e menor

lista = []

for cont in range(1, 6):
    peso = float(input("O pesoa da {}° pessoa é: ".format(cont)))
    lista.append(peso)

lista.sort()

print("\nMaior peso: {}\nMenor peso: {}".format(lista[4], lista[0]))