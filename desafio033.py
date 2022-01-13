# Programa que recebe 3 números como entrada, devolvendo
# como saída o maior e o menor

n_1 = int(input("Primeiro valor: "))
n_2 = int(input("Segundo valor: "))
n_3 = int(input("Terceiro valor: "))

lista_de_numeros = [n_1, n_2, n_3]
lista_de_numeros.sort()

# O comando .sort() ordena do menor para  o maior a lista

print("Maior valor digitado: {}\nMenor valor digitado: {}".format(lista_de_numeros[2], lista_de_numeros[0]))