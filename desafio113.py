# Programa que recebe de entrada um dado qualquer, dando erro até
# receber um inteiro e um real, devolvendo-os depois

def inteiro(mensagem):
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


def real(mensagem):
    while True:
        try:
            num = float(input(mensagem))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número inteiro válido.\033[m")
            continue
        except(KeyboardInterrupt):
            print("\n\033[31mUsuário preferiu não digitar esse número.\033[m")
            return 0
        else:
            return num


numero1 = inteiro("Digite um valor inteiro: ")
numero2 = real("Digite um valor real: ")
print(f"O valor inteiro digitado foi {numero1} e o real {numero2}")