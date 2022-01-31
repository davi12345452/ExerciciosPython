# Programa recebe um nome e uma media de notas de entrada,
# devolvendo como saída a situação - FEITO EM DICIONÁRIO

aluno_dici = {}

aluno_dici["Nome"] = str(input("Digite o nome do aluno: "))
aluno_dici["Media"] = float(input("Digite a media do aluno: "))

situacao = ""

# Considerei a media como 6

if aluno_dici["Media"] >= 6:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"


print("\nNome:",aluno_dici["Nome"])
print("Media:", aluno_dici["Media"])
print("Situação:", situacao)

