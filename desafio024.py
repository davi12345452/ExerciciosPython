# Programa recebe como entrada o nome de uma cidade, devolvendo
# como saída se a cidade começa ou não a palavra "Santo" no nome

cidade = str(input("Digite a cidade em que você nasceu: ")).split()
santo = cidade[0].upper()

if santo == "SANTO":
    print("True")
else:
    print("False")

