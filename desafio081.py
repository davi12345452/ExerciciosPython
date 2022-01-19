# Programa que recebe de entrada x números, devolvendo como
# saída a quantidade de números, a lista decrescente e se o
# número 5 faz parte desta lista

lista = []
count = 0

while True:
    num = int(input("Digite um número: "))
    lista.append(num)
    count += 1
    continuar = str(input("Deseja continuar?[S]/[N] ")).upper()
    if continuar == "N":
        break

lista.sort()
lista_invertida = []

for num in lista:
    lista_invertida.insert(0, num)


print(count)
print(lista_invertida)

if 5 in lista:
    print(True)
else:
    print(False)

