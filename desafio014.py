# Programa recebe uma temperatura em C° como entrada
# devolvendo-a em F° como saída

temp_c = float(input("Digite a temperatura em C°: "))

temp_f = ((9 * temp_c) / 5) + 32

print("O valor da temperatura de {:.2f}C° em Farenheit é {:.2f}F°".format(temp_c, temp_f))