# Programa recebe o valor de um produto e um desconto em %
# como entrada e devolve o valor aplicado com o desconto co-
# como saída

valor = float(input("Digite o valor do produto em R$: "))
desconto = float(input("Digite o valor do desconto em %: "))

desconto_aplicado = valor * ((100 - desconto) / 100)

print(f"O valor do produto, com {desconto}% de desconto ficou R${desconto_aplicado}")