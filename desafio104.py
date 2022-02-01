# Programa que define uma função que recebe uma entrada e verifica
# se ela é um número inteiro


def eh_int(mensagem):
    condicao = False
    while condicao is False:
        num = str(input(mensagem))
        if num.isnumeric():
            print(f"O número {num} é VÁLIDO")
            condicao = True
        else:
            print("\033[0;31mERRO! Digite um número válido\033[m")


eh_int("Digite um número: ")



