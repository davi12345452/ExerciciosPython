# Programa que recebe de entrada o peso e altura da pessoa, devolvendo
# como saída o IMC desta

peso = float(input("Peso em kg: "))
altura = float(input("Altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("CUIDADO, você está ABAIXO DO PESO.")
elif 18.5 <= imc < 25:
    print("PARABENS, você está no PESO IDEAL.")
elif 25 <= imc < 30:
    print("ATENÇÃO, você está no SOBREPESO.")
elif 30 <= imc < 40:
    print("CUIDADO, você está em OBESIDADE.")
elif imc > 40:
    print("EXTREMO CUIDADO, você está em OBESIDADE MÓRBIDA.")