# Programa que recebe 3 comprimentos como entrada, devolvendo como
# saída se podem formar um triângulo e qual tipo

lado_1 = float(input("Primeiro lado: "))
lado_2 = float(input("Segundo lado: "))
lado_3 = float(input("Terceiro lado: "))

lista = [lado_1, lado_2, lado_3]
lista.sort()

if (lista[0] + lista[1]) >= lista[2]:
    if lista[0] == lista[1] == lista [2]:
        print("Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO")
    elif lista[0] != lista[1] and lista[0] != lista[2] and lista[1] != lista[2]:
        print("Os segmentos acima PODEM FORMAR um triângulo ESCALENO")
    else:
        print("Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo")