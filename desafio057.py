# Programa que recebe como entrada um sexo e devolve como saída,
# que o programa registrou com sucesso o sexo da pessoa

sexo = str(input("Digite o seu sexo [M]/[F]")).upper()
while True:
    if sexo == "M" or sexo == "F":
        print("Sexo registrado com sucesso")
        break
    sexo = str(input("Dados Inválidos. Digite seu sexo novamente [M]/[F]")).upper()
