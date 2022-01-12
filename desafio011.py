# Esse programa recebe com entrada as dimensões de
# parede e devolve como saída a área dessa mesma
# parede e a quantidade de tinta em litro necessá-
# ria para pintar, levando em conta 1 m2 = 0,5 L

altura = float(input("Altura da parede em metros: "))
largura = float(input("Largura da parede em metros: "))

area = largura * altura
tinta = area / 2

print("A parede {} x {}, de área {} metros quadrados precisa\nde {} litros de tinta para ser pintada ".format(altura, largura, area, tinta))
