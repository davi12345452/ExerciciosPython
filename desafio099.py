# Programa que define uma função que recebe uma quantidade de números como
# entrada, a pessoa cadastra-os, devolvendo como saída a quantidade de
# número e o maior deles


def math_function(* num):
    lista = list()
    for valor in num:
        lista.append(valor)
    lista.sort()
    print(f"Foram informados {len(lista)} números, sendo o maior {lista[-1]}")


math_function(1, 22, 4, 5, 6, 7)
math_function(1, 22, 44, 5, 6, 7)
math_function(1, 22, 4, 5, 6, 7)
math_function(1, 22, 4, 65, 6, 7)
math_function(1, 22, 4, 5, 86, 7)
math_function(1, 22, 4, 5, 696, 7)
