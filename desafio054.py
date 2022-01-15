# Programa recebe de entrada o ano de nascimento de 7 pessoas
# devolvendo como saída quantas são maiores de idade e quantas
# são menores de idade

from datetime import date

ano_atual = date.today().year
maior = 0
menor = 0

for cont in range(1, 8):
    ano = int(input("Em que ano a {}° pessoa nasceu: ".format(cont)))
    if ano_atual - ano >= 18:
        maior += 1
    else:
        menor += 1

print("\nAo todo tivemos {} pessoas maiores de idade".format(maior))
print("\nAo todo tivemos {} pessoas menores de idade".format(menor))
