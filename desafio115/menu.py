# Menu do programa


def linha(tam=40):
    return '-' * tam


def leia_inteiro(mensagem):
    while True:
        try:
            num = int(input(mensagem))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número inteiro válido.\033[m")
            continue
        except(KeyboardInterrupt):
            print("\n\033[31mUsuário preferiu não digitar esse número.\033[m")
            return 0
        else:
            return num


def cabecalho(texto):
    print(linha())
    print(texto.center(40))
    print(linha())


def layout(lista):
    cabecalho("MENU PRINCIPAL")
    cont = 1
    for elem in lista:
        print(f"\033[33m{cont}- \033[34m{elem}\033[m")
        cont += 1
    print(linha())
    opcao = leia_inteiro("Sua opção: ")
    return opcao


