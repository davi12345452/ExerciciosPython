# Progrma recebe como entrada 5 números, colocando-os em
# um lista e devolvendo o maior e menor

lista_num = []

for count in range(5):
    num = int(input("Digite o número na posição {}: ".format(count)))
    lista_num.append(num)

print("Lista: ", lista_num)
lista_num.sort()
print("Maior: {}\n"
      "Menor: {}".format(lista_num[-1], lista_num[0]))