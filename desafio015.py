# Programa recebe como entrada os dias de aluguel de um carro
# e quantos quilometros foram rodados, devolvendo como saída
# o valor a pagar pelo aluguel

dias = int(input("Quantos dias ficou com o carro: "))
km = float(input("Quantos kilômetros rodou com o carro: "))

pagar = (60 * dias) + (km * 0.15)

print("O total a pagar pelo carro foi de R${:.2f}".format(pagar))