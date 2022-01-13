# Programa recebe uma frase como entrada, devolvendo
# uma análise da aparição da letra A como saída

# Comandos .find e .rfind acham a primeira e última aparição
# de algo em uma string respectivamente

# Comando .count conta o número de aparições de uma letra
# ou termo.

frase = str(input("Digite uma frase: ")).upper()
print("A frase possui {} letras A".format(frase.count("A")))
print("A primeira letra A apareceu na posição {}".format(frase.find("A") + 1))
print("A última letra A apareceu na posição {}".format(frase.rfind("A") + 1))

# Soma-se 1 pelo fato de strings começarem na posição 0
