# Programa recebe como entrada uma frase, devolvendo como saída
# se a frase é ou não um Palíndromo, além de mostrar a frase ao
# inverso

frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = "" .join(palavras)
inverso = ""

for cont in range(len(junto) - 1, -1, -1):
    inverso += junto[cont]

print("O inverso de {} é {}".format(junto, inverso))
if inverso == junto:
    print("A frase é um PALÍNDROMO")
else:
    print("A frase NÃO é um PALÍNDROMO")