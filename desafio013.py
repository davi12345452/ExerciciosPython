# Programa recebe como entrada um salário e o valor em % do
# aumento, dando como saída o novo salário

salario = float(input("Valor do salário em R$: "))
aumento = float(input("Valor do aumento e %: "))

aumento_salario = salario * ((100 + aumento) / 100)

print("O novo salário, com aumento de {}% será de R${:.2f}".format(aumento, aumento_salario))