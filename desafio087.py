# Programa que recebe de entrada 9 termos para preencher uma matriz 3x3,
# devolvendo essa matriz de saída, além de observações acerca da mesma

array = []

# Construção do Array

for count1 in range(3):
    new_array = []
    for count2 in range(3):
        num = int(input("Digite um valor para [{}, {}]: ".format(count1, count2)))
        new_array.append(num)
    array.append(new_array)

# Impressão do Array

print("-="*20)

for line in array:
    for number in line:
        print("[{:^5}]".format(number), end="")
    print("")

print("-="*20)

par = 0
linha2 = 0
linha3 = 0

for linha in array:
    for num in linha:
        if linha == array[2]:
            linha3 += num
        if linha == array[1]:
            linha.sort()
            linha2 = linha[2]
        if num % 2 == 0:
            par += num

print("Soma dos pares = ", par)
print("Maior da 2 linha = ", linha2)
print("Soma da 3 linha = ", linha3)