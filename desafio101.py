# Programa que define uma função que recebe de entrada um ano de nascimento e
# calcula se a pessoa deve ou não votar, devolvendo a resposta como saída

from datetime import date


def votacao(ano):
    idade = date.today().year - ano
    if idade >= 18:
        print(f"Com {idade} anos: VOTO OBRIGATÓRIO")
    elif idade >= 16:
        print(f"Com {idade} anos: VOTO OPCIONAL")
    else:
        print(f"Com {idade} anos: VOTO PROIBIDO")


votacao(2001)
votacao(2006)
votacao(2010)
votacao(1960)
votacao(2003)