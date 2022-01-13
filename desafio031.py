# Programa que calcula o valor de uma passagem de viagem de acordo com
# a distância percorrid

distancia = int(input("Digite aqui a distância em km de sua viagem: "))

preco = None

if distancia > 200:
    preco = 0.45 * distancia
else:
    preco = 0.5 * distancia

print(f"Você está prestes a começar uma viagem de {distancia} km")
print(f"E o preço de sua passagem será R${preco}")