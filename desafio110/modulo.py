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


def resumo(valor, aum, red):
    print("-"*30)
    print("RESUMO DO VALOR".center(30))
    print("-" * 30)
    print(f"Preço analisado: \t{moeda(valor)}")
    print(f"Dobro do preço: \t{dobro(valor, True)}")
    print(f"Metade do preço: \t{metade(valor, True)}")
    print(f"Aumento de {aum}%: \t{juros(True, aum, valor, True)}")
    print(f"Redução de {red}%: \t{juros(False, red, valor, True)}")
    print("-" * 30)