# Programa que recebe como entrada um número e devolve como
# saída o seu fatorial

num = int(input("Digite um número: "))
multiplicador = num
fatorial = 1

for count in range(num):
    multiplicador = num - count
    fatorial *= multiplicador
    if count == (num - 1):
        print(f"{multiplicador} =", end=" ")
        break
    print(f"{multiplicador} x", end=" ")

print(fatorial)