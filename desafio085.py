# Programa que recebe 7 números, criando duas listas com eles,
# uma de pares e outra de ímpares, devolvendo-as como saída

lista_par = []
lista_imp = []

for count in range(1, 8):
    num = int(input("Digite o {}o. número: ".format(count)))
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_imp.append(num)

print("Pares: ",lista_par)
print("Ímpares: ",lista_imp)