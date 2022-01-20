# Programa recebe de entrada alguns números, devolvendo como
# saída a lista completa, uma lista de par e de ímpar

lista = []

while True:
    num = int(input("Digite um número: "))
    lista.append(num)
    continuar = str(input("Você deseja continuar?[S]/[N] ")).upper()
    if continuar == "N":
        break

lista_par = []
lista_impar = []

for num in lista:
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)

print("Lista completa: ",lista)
print("Lista de número ímpar: ",lista_impar)
print("Lista de número par: ",lista_par)

