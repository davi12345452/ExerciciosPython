# Programa que recebe dados de entrada para o cadastro de uma pessoa,
# devolvendo como saída esse mesmo cadastro

from datetime import date

dados_trabalhador = {}
ano_atual = date.today().year

dados_trabalhador["Nome"] = str(input("Nome: "))
dados_trabalhador["Idade"] = ano_atual - int(input("Ano de nascimento: "))
dados_trabalhador["Carteira de Trabalho"] = int(input("Carteira de trabalho (digite 0 se não tem): "))

if dados_trabalhador["Carteira de Trabalho"] != 0:
    dados_trabalhador["Ano de Contratação"] = int(input("Ano de contratação: "))
    dados_trabalhador["Salario"] = float(input("Salário: R$"))
    dados_trabalhador["Aposentadoria"] = (35 - (ano_atual - dados_trabalhador["Ano de Contratação"])) + dados_trabalhador["Idade"]
else:
    dados_trabalhador["Carteira de Trabalho"] = "Não possui carteira de trabalho"

print("-="*20)

for chave, cont in dados_trabalhador.items():
    print(f"{chave} tem o valor {cont}")


