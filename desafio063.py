# Programa que recebe de entrada um número de entrada e devolve com saída
# um sequência de fibonacci com o número de termos imputados

n_1 = 0
n_2 = 1
n_3 = n_2 + n_1

print("-"*30)
print("Sequência de Fiboanacci")
print("-"*30)

termos = int(input("Quantos termos você quer mostrar? "))
print("~"*30)

for count in range(termos):
    print(n_1, end=" -> ")
    n_1 = n_2
    n_2 = n_3
    n_3 = n_1 + n_2

print("FIM")
print("~"*30)