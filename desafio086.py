# Programa que recebe de entrada 9 valores, devolvendo de saída
# esses números organizados em uma matriz 3x3

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
