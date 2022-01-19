# Programa que verifica as vogais presentes em palavras. Não há uma
# entrada, apenas a saída

palavras = ("Davi", "Casa", "Cachorro", "Chocolate", "Entender", "Bebida",
            "Refrigerante")

vogais = ("A", "E", "I", "O", "U")

for palavra in palavras:
    new_palavra = palavra.upper()
    print("Na palavra {} temos as vogais: ".format(new_palavra), end="")
    for vogal in vogais:
        if vogal in new_palavra:
            print(vogal, end=" ")
    print("")