# Programa que recebe de entrada um valor que diz a quantidade de sorteios de números
# devolvendo uma lista com os números sorteados e a soma dos pares


from random import randint


def pares(num):
    lista = list()
    soma_pares = 0
    for cont in range(num):
        novo = randint(0, 10)
        lista.append(novo)
        if novo % 2 == 0:
            soma_pares += novo
    print(f"Foram sorteados {num} números, os quais são: {lista}")
    print(f"Somando os valores pares de {lista} temos {soma_pares}")


pares(10)
pares(3)
pares(19)
pares(13)