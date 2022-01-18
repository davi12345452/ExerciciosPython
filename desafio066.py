# Programa que recebe infinitos números, se assim o usuário desejar, e
# devolve como saída a soma destes

soma = 0
termos = 0
num = 0

while num != 999:
    num = int(input("Digite um número [999 para parar]: "))
    if num != 999:
        soma += num
        termos += 1


print(f"Você digitou {termos} números, sendo sua soma igual a {soma}")