# Não recebe entrada, apenas a execução do programa, devolvendo
# como saída uma classificação  e algumas modificações

classificacao = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
                'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
                'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama',
                'Sport Recife', 'América-MG', 'Chapecoense', 'Vitória', 'Paraná')

print("-=" * 15)
print("Lista de times do brasileirão: {}".format(classificacao))

print("-=" * 15)
primeiros_5 = classificacao[:4]
print("Os 5 primeiros classificados foram: ", primeiros_5)

print("-=" * 15)
ultimos_4 = classificacao[-4:]
print("Os 4 últimos classficados foram: ", ultimos_4)

print("-=" * 15)
ordem_alfabetica = []
for time in classificacao:
    ordem_alfabetica.append(time)
ordem_alfabetica.sort()
print("A ordem alfabética dos times é: ", ordem_alfabetica)

print("-=" * 15)
chape = 0
for time in classificacao:
    chape += 1
    if time == "Chapecoense":
        break
print("A chapecoense está na {}° posição".format(chape))
print("-=" * 15)
