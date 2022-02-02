# Programa que recebe de entrada um comando, devolvendo como saída
# uma explicação acerca desse comando. Caso o usuário queira encerrar
# o programa, basta digitar "fim"


def ajuda(com):
    help(com)


while True:
    comando = str(input("Digite o comando: "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)

