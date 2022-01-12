# Pitágoras: programa recebe como entrada o valor dos
# catetos, devolvendo como saída o valor da hipotenusa

c_oposto = float(input("Cateto Oposto: "))
c_adjacente = float(input("Cateto Adjecente: "))

from math import sqrt

hipotenusa = sqrt((c_oposto ** 2) + (c_adjacente ** 2))

print("O valor da hipotenusa será de {:.2f}".format(hipotenusa))