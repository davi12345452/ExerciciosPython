# Programa que recebe de entrada 4 números, coloca-os em uma
# tupla e depois faz uma análise, devolvendo constatações
# acerca deles

num_1 = int(input("Primeiro Número: "))
num_2 = int(input("Segundo Número: "))
num_3 = int(input("Terceiro Número: "))
num_4 = int(input("Último Número: "))

tupla = (num_1, num_2, num_3, num_4)

print("Você digitou os valores:", tupla)

print("O número 9 apareceu {} vezes na tupla".format(tupla.count(9)))

if 3 in tupla:
    print("O número 3 aparece na tupla, na posição", tupla.index(3) + 1)
else:
    print("O número 3 não aparece na tupla.")

pares = 0
for num in tupla:
    if num % 2 == 0:
        pares += 1
print("Foram digitados {} números pares".format(pares))