# Programa que recebe de entrada pessoas como cadastro, seu nome e peso
# adicionando-os em uma lista composta. Como saída, o programa devolve
# o número de cadastros, o maior e menor peso

lista_composta = []

while True:
    nome = str(input("Digite o nome: "))
    peso = int(input("Digite o peso: "))
    lista = []
    lista.append(peso)
    lista.append(nome)
    lista_composta.append(lista)
    continuar = str(input("Deseja continuar?[S]/[N] ")).upper()
    if continuar == "N":
        break

print("Ao todo você cadastrou {} pessoas.".format(len(lista_composta)))

lista_maior = []
lista_menor = []

lista_composta.sort()

for elem in lista_composta:
    if elem[0] == lista_composta[0][0]:
        lista_menor.append(elem)
    elif elem[0] == lista_composta[-1][0]:
        lista_maior.append(elem)

print("O menor peso foi de {}kg, o peso de ".format(lista_menor[0][0]), end="")
for elem in lista_menor:
    print(elem[1], end=" ")
print("")
print("O maior peso foi de {}kg, o peso de ".format(lista_maior[0][0]), end="")
for elem in lista_maior:
    print(elem[1], end=" ")





