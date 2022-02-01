# Programa que define uma função que calcula a área de
# um terreno utilizando sua largura e comprimento

def area(l, c):
    return l * c


largura = float(input("Largura: "))
comprimento = float(input("Comprimento: "))
print(area(largura, comprimento))