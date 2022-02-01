# Programa que cria uma função que recebe de entrada um número para
# mostrar o fatorial, além de outra entrada que expoe as contas ou não

def fatorial(num, show):
    numero = num
    if show is True:
        print(numero, end = " ")
        for cont in range((num - 1), 0, -1):
            print(f"x {cont}", end=" ")
            numero *= cont
        print(f"= {numero}")
    else:
        for cont in range((num - 1), 0, -1):
            numero *= cont
        print(numero)


fatorial(10, True)
fatorial(20, show=True)
fatorial(10, show=False)
fatorial(20, False)