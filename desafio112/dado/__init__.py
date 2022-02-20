# Funções


def leitor(mensagem):
    verif = False
    while not verif:
        entrada = str(input(mensagem)).replace(',', '.')
        if entrada.isalpha():
            print(f"\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m")
        else:
            verif = True
            return float(entrada)









