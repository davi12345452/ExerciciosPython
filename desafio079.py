# Programa que recebe indeterminados números de entrada, devolvendo
# uma lista sem valores duplicados

lista_num = []

while True:
    num = int(input("Digite um número: "))
    if num in lista_num:
        print("Valor duplicado, não foi adicionado")
    else:
        lista_num.append(num)
        print("Valor {} adicionado à lista".format(num))
    continuar = str(input("Deseja continuar adicionando? [S]/[N] ")).upper()
    if continuar == "N":
        break

print("Você adicionou os valors: ", lista_num)