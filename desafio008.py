# O usuário digita uma distância em metros como entrada
# e recebe como saída o seu valor em km, hm, dam, dm, cm
# e mm

distancia = float(input("Digite a distância em metros: "))

print(f"A distância de {distancia} metros corresponde a: \n"
      f"{(distancia * 0.001)} km\n"
      f"{(distancia * 0.01)} hm\n"
      f"{(distancia * 0.1)} dam\n"
      f"{(distancia * 10)} dm\n"
      f"{(distancia * 100)} cm\n"
      f"{(distancia * 1000)} mm")

# Resolvi mudar e fazer os comandos dentro do print

