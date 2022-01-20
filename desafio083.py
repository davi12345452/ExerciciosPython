# Programa que recebe como entrada uma expressão, devolvendo
# como saída se é válida ou não.

exp = str(input("Digite uma expressão: "))

if exp.count("(") == exp.count(")"):
    print("Você digitou uma expressão válida!")
else:
    print("Você digitou uma expressão inválida")