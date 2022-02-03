# Programa que funciona em módulos, nesse arquivo apenas vou definir
# as funções, sendo no desafio108-__init__.py onde vou aplicar essas
# funções como módulo.


def moeda(valor=0, moeda = "R$"):
    return f"{moeda}{valor:.2f}".replace(".", ",")


def juros(sit, juro, valor):
    # True = aumentar
    if sit is True:
        valor *= (juro/100 + 1)
    # False = diminuir
    else:
        valor *= (1 - juro/100)
    return valor


def metade(valor):
    valor *= 0.5
    return valor


def dobro(valor):
    valor *= 2
    return valor
