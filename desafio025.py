# Programa recebe de entrada um nome completo, devolvendo
# como saída se há ou não o nome "Silva" neste nome.

nome = str(input("Digite seu nome completo: ")).upper().split()
contador = len(nome)

verificador = None

while contador != 0:
    if nome[contador - 1] == "SILVA":
        verificador = True
    contador -= 1

if verificador is True:
    print("Seu nome tem Silva? True")
else:
    print("Seu nome tem Silva? False")