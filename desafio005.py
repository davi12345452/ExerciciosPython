# Esse progrma recebe como entrada um número inteiro e
# da como saída o seu antecessor e seu sucessor

numero = int(input("Digite um número inteiro: "))

antecessor = numero - 1
sucessor = numero + 1

# Essa soma poderia ser feita dentro do format

print("O antecessor do número {} é o {} e seu sucessor é {}".format(numero, antecessor, sucessor))
