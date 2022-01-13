# Conversor de base: programa recebe um número em decimal, podendo
# devolver como saída esse número em octal, binário ou hexadecimal

numero = int(input("Digite um número que queira converter: "))
print("\n[1] - Converter em BINÁRIO\n[2] - Converter em OCTAL\n[3] - Converter em HEXADECIMAL")
decisao = int(input("\nSua opção: "))

if decisao == 1:
    binario = bin(numero)
    print("\n{} em BINÁRIO = {}".format(numero, binario))
elif decisao == 2:
    octa = oct(numero)
    print("\n{} em OCTAL = {}".format(numero, octa))
elif decisao == 3:
    hexa = hex(numero)
    print("\n{} em HEXADECIMAL = {}".format(numero, hexa))
else:
    print("Você digitou uma opção inválida.")