# Programa que recebe de entrada um número inicial e uma razão, devolvendo
# como saída uma PA de 10 termos com estas informações

print("=="*10)
print("10 TERMOS DE UMA PA")
print("=="*10)

razao = float(input("Razão da PA: "))
termo_incial = float(input("Termo Inicial da PA: "))

for cont in range(10):
    print((termo_incial + (razao * cont)), end=" -> ")

print("Acabou")