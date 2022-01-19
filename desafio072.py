# Programa que recebe de entrada um número, devolvendo como saída
# o seu nome por extenso

numeros = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')

while True:
    entrada = int(input("Digite um número de 0 a 20: "))
    if 0 <= entrada <= 20:
        break
    else:
        print("Tente novamente, você digitou um número inválido.")

print("Você digitou o número {}".format(numeros[entrada]))