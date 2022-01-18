# Programa de cadastro: programa recebe como entrada, dados de pessoas,
# devolvendo como saída algumas comparações

lista = []
while True:
    print("--" * 15)
    print("\tCADASTRO DE PESSOAS")
    print("--" * 15)
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: [M]/[F] ")).upper()
    print("--" * 15)
    lista_provisoria = [idade, sexo]
    lista.append(lista_provisoria)
    parar = str(input("Deseja continuar? [S]/[N] ")).upper()
    if parar == "N":
        break

p_18 = 0
homem = 0
m_20 = 0

for count in lista:
    if count[0] > 18:
        p_18 += 1
    if count[1] == "M":
        homem += 1
    else:
        if count[0] < 20:
            m_20 += 1

print(f"Total de pessoas com mais de 18 anos: {p_18}")
print(f"Ao todo temos {homem} homens cadastrados.")
print(f"E temos {m_20} mulheres com menos de 20 anos.")




