# Esse programa recebe 2 notas de um aluno como entrada e
# calcula a sua media como saída, verificando se o aluno
# foi ou não aprovado pela media 6.0

nota1 = float(input("A primeira nota: "))
nota2 = float(input("A segunda nota: "))

media = (nota1 + nota2) / 2

print("Tendo como notas um {} e um {}, a media do aluno foi {}".format(nota1, nota2, media))

if media >= 6.0:
    print("O aluno foi APROVADO")
else:
    print("O aluno NÃO foi APROVADO")