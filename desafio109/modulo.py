# Funções

def moeda(valor=0, moeda = "R$"):
    return f"{moeda}{valor:.2f}".replace(".", ",")


def juros(sit, juro, valor, formato=False):
    # True = aumentar
    if sit is True:
        valor *= (juro/100 + 1)
    # False = diminuir
    else:
        valor *= (1 - juro/100)
    return valor if formato is False else moeda(valor)


def metade(valor, formato=False):
    valor *= 0.5
    return valor if formato is False else moeda(valor)


def dobro(valor, formato=False):
    valor *= 2
    return valor if formato is False else moeda(valor)
