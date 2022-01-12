# Neste programa o usuário dá como entrada
# dois números e recebe como saída a sua soma

num_1 = float(input("Digite um número: "))
num_2 = float(input("Digite outro número: "))

soma = num_1 + num_2

# A soma poderia estar dentro do format do print

print("\nA soma de {} e {} é igual a {}.".format(num_1, num_2, soma))