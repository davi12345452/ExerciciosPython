# Programa que recebe 3 lados com quaisquers tamanhos como entrada
# devolvendo se eles podem ou não formar um triângulo

l1 = float(input("Primeiro lado: "))
l2 = float(input("Segundo lado: "))
l3 = float(input("Terceiro lado: "))

lista = [l1, l2, l3]
lista.sort()

if lista[2] > (lista[0] + lista[1]):
    print("NÃO podem formar um triângulo.")
else:
    print("Podem formar um triângulo.")