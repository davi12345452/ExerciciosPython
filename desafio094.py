# Programa completo de cadastro de pessoas, que mescla dicionários
# dentro de uma lista

lista = list()
dicionario = dict()
soma_idades = 0

while True:
    dicionario.clear()
    dicionario["nome"] = str(input("Nome: "))
    dicionario["idade"] = int(input("Idade: "))
    soma_idades += dicionario["idade"]
    while True:
        dicionario["sexo"] = str(input("Sexo[M/F]")).upper()
        if dicionario["sexo"] in "MF":
            break
        print("ERRO, digite seu sexo novamente")
    while True:
        resposta = str(input("Deseja continuar cadastrando?[S/N] ")).upper()
        if resposta in "SN":
            break
        print("ERRO, digite sua resposta novamente")
    lista.append(dicionario.copy())
    if resposta == "N":
        break

print("-"*40)

num_cadastrados = len(lista)
print(f"A) Ao todos temos {num_cadastrados} pessoa(s) cadastrada(s).")

media = soma_idades/num_cadastrados
print(f"B) A média de idades é de {media} anos.")

print("C) As mulheres cadastradas foram ", end="")
for elem in lista:
    if elem["sexo"] == "F":
        print(elem["nome"], end=" ")
print("")

print("D) Lista das pessoas que estão acima da média de idade")
for elem in lista:
    if elem["idade"] > media:
        for key, cont in elem.items():
            print(f"{key} : {cont}", end=" ")
    print("")

print("\n\nENCERRADO")