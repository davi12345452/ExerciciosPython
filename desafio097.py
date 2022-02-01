# Programa que define uma funação que recebe uma string
# devolvendo-a como saída, porém com alguns enfeites

def escreva(texto):
    print("^"*len(texto))
    print(texto)
    print("^" * len(texto))


mensagem = str(input("Digite a mensagem que deseja personalizar: "))
escreva(mensagem)
    