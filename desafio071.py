# Programa que recebe de entrada um valor e devolve esse valor em cedulas
# buscando sempre o menor número destas na saída

print("==" * 15)
print("\t  BEM VINDO AO BANCO")
print("==" * 15)

valor = int(input("Digite o valor que deseja sacar: R$"))
tipos_de_cedulas = [200, 100, 50, 20, 10, 5, 2, 1]


for nota in tipos_de_cedulas:
    cedula = valor // nota
    valor -= cedula * nota
    if cedula != 0:
        print(f"Total de {cedula} cédulas de R${nota}")
    if valor == 0:
        break

print("==" * 15)
print("Volte sempre ao BANCO")