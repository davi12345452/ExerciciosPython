# Programa que recebe de entrada nome e notas dos alunos,
# devolvendo como saída um boletim com media, possibilitando
# a visualização individual de cada um.

lista = []

while True:
    nova_lista = []
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nova_lista.append(nome)
    nova_lista.append(nota1)
    nova_lista.append(nota2)
    lista.append(nova_lista)
    pergunta = str(input("Deseja continuar cadastrando?[S/N] ")).upper()
    if pergunta == "N":
        break

count = 0

print("-="*30)
print("%-4s%-15s%-10s" % ("No.", "NOME", "MÉDIA"))
print("-"*29)
for linha in lista:
    print("%-4d%-15s%-10.2f" % (count, linha[0], ((linha[1] + linha[2])/2)))
    count += 1
print("-"*29)

while True:
     num = int(input("Mostrar a nota de qual aluno(999 interrompe): "))
     if num == 999:
         break
     print(f"Notas de {lista[num][0]} são: {lista[num][1]} e {lista[num][2]}")

