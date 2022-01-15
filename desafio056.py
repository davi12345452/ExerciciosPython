# Analisador, programa recebe informações de 4 pessoas, devolvendo
# como saída 3 comparações acerca das informações

nomes = []
idades = []
sexos = []

for cont in range(1, 5):
    print("=" * 6, "{} PESSOA".format(cont), "=" * 6)
    nome = str(input("Nome: "))
    nomes.append(nome)
    idade = int(input("Idade: "))
    idades.append(idade)
    sexo = str(input("Sexo[M]/[F]: ")).upper()
    sexos.append(sexo)

media = sum(idades) / len(idades)

print("A media de idade é: {} anos".format(media))

h_maior_idade = 0
cont_lista = None
n_mulher = 0

for cont in range(0, 4):
    if sexos[cont] == "M":
        if h_maior_idade < idades[cont]:
            h_maior_idade = idades[cont]
            cont_lista = cont
    else:
        if idades[cont] < 20:
            n_mulher += 1

print("O homem mais velho, com {} anos é o {}".format(h_maior_idade, nomes[cont_lista]))
print("Ao todo, são {} mulheres com menos de 20 anos".format(n_mulher))


