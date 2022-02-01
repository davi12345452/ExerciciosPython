# Programa que define uma função de contagem, recebe de entrada
# o início e fim, além de quantos números pular

def contagem(inicio, fim, pular):
    print("-="*20)
    if inicio > fim:
        pular = - pular
    print(f"Contagem de {inicio} até {fim} de {pular} em {pular}")
    for cont in range(inicio, fim, pular):
        print(cont, end=" ")
    print("FIM!")
    print("-=" * 20)


i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))

contagem(i, f, p)