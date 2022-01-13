# Programa que recebe como entrada o ano de nascimento de um atleta
# devolvendo como saída a sua idade e classificação

from datetime import date

ano = int(input("Ano de nascimento: "))
idade = date.today().year - ano

print("O atleta tem {} anos".format(idade))

if idade <= 9:
    print("Classificação: Mirim")
elif 9 < idade <= 14:
    print("Classificação: Infantil")
elif 14 < idade <= 19:
    print("Classificação: Junior")
elif 19 < idade <= 25:
    print("Classificação: Sênior")
else:
    print("Classificação: Master")