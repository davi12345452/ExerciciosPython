# Programa que recebe um número positivo de entrada e devolve como saída
# a sua tabuado. Detalhe, este programa está em um loop, ou seja, o usuá-
# irio irá ver infinitas tabuadas diferentes se desejar. Basta digitar um
# número negativo para parar o loop e encerrar o programa

while True:
    print("--" * 20)
    num = int(input("Quer ver a tabuada de qual valor: "))
    print("--" * 20)
    if num < 0:
        break
    else:
        for count in range(1, 11):
            print(f"{num} x {count} = {num * count}")

print("PROGRAMA TABUADA ENCERRADO. Volte sempre!")