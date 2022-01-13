# Programa recebe um número entre 9999 e 1, devolvendo
# como saída seu milhar, centena, dezena e unidade.

numero = int(input("Digite um número inteiro: "))

# O programa vai fazer a divisão sem resto e depois retirar o valor do número
# Por exemplo, se milhar for 4, ele vai analisar e depois retirar 4000 do número

milhar = numero // 1000
numero -= milhar * 1000
centena = numero // 100
numero -= centena * 100
dezena = numero // 10
numero -= dezena * 10
unidade = numero // 1

print("\nMilhar: %d\nCentena: %d\nDezena: %d\nUnidade: %d" % (milhar, centena, dezena, unidade))

