# Programa que recebe quantos números o usuário desejar dar de entrada
# devolvendo sua media, o maior e o menor termo

lista_num = []

while True:
    num = int(input("Digite um número: "))
    lista_num.append(num)
    continuar = str(input("Quer continuar? [S]/[N] ")).upper()
    if continuar == "N":
        break

media = float(sum(lista_num) / len(lista_num))
print(f"\nVocê digitou {len(lista_num)} números, sendo sua média igual a {media}")
lista_num.sort()
print(f"O maior valor foi {lista_num[-1]} e o menor valor foi {lista_num[0]}")