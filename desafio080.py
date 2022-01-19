# Programa recebe 5 números de entrada, adiciona-os de maneira
# inversa na lista, devolvendo como saída essa lista em ordem

lista = []

for count in range(5):
    num = int(input("Digite o numero: "))
    if count == 0 or num > lista[-1]:
        lista.append(num)
    else:
        for pos, x in enumerate(lista):
            if num <= x:
                lista.insert(pos, num)
                break
print(lista)
