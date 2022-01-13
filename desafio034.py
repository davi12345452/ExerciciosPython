# Programa que recebe como entrada um salário, devolvendo como saída
# esse salário corrigido por um aumento, que varia de acordo com o ta-
# manho atual dos salários

salario = float(input("Digite o seu salário em R$: "))

if salario > 1250:
    salario = 1.10 * salario
else:
    salario = 1.15 * salario

print("Seu novo salário será de R${:.2f}".format(salario))