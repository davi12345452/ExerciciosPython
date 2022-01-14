# Programa que mostra em cadeia todos os números pares até 50
# não recebe entrada

for cont in range(1, 51):
    if cont % 2 == 0:
        print(cont, end=" -> ")

print("ACABOU")