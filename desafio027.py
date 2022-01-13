# Programa que recebe como entrada um nome completo, devolvendo
# como saída o primeiro e último nome da pessoa

nome = str(input("Digite o seu nome completo: ")).split()

primeiro_n = nome[0]
ultimo_n = nome[len(nome) - 1]

print("\nSeu primeiro nome: %s\nSeu último nome: %s" % (primeiro_n, ultimo_n))