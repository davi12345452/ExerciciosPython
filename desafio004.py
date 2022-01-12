# Programa irá receber qualquer coisa
# como entrada e dará algumas informa-
# ções sobre, como a classe, se é um
# número...

entrada = input("Digite algo: ")

print("O tipo de dado digitado é: {}".format(type(entrada)))
print("Só tem espaços? {}".format(entrada.isspace()))
print("É um número? {}".format(entrada.isnumeric()))
print("É alfabético? {}".format(entrada.isalpha()))
print("É alfanumérico? {}".format(entrada.isalnum()))
print("Está em maiúsculas? {}".format(entrada.isupper()))
print("Está em minúsculas? {}".format(entrada.islower()))
print("Está capitalizado? {}".format(entrada.istitle()))