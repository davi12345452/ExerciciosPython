# Programa que recebe de entrada o nome do produto e seu valor
# devolvendo como saída algumas constações acerca do pedido

print("\033[1m--" * 15)
print("\t\033[1m  LOJA SUPER BARATÃO")
print("\033[1m--" * 15)

precos_nomes = []
maior_que_mil = 0

while True:
    nome = str(input("Nome do produto: "))
    preco = int(input("Preço: R$"))
    lista = [preco, nome]
    precos_nomes.append(lista)
    if preco > 1000:
        maior_que_mil += 1
    resposta = str(input("Deseja continuar: [S]/[N] ")).upper()
    if resposta == "N":
        print("\033[1m-" * 6, " FIM DO PROGRAMA ", "\033[1m-" * 5)
        break

total = 0
for price in precos_nomes:
    total += price[0]

precos_nomes.sort()

print(f"\nO total da compra foi R${total}")
print(f"Temos {maior_que_mil} produto que custa mais que R$1000,00")
print(f"O produto mais barato foi {precos_nomes[0][1]} que custou R${precos_nomes[0][0]}")