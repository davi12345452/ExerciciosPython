# Esse programa recebe um número qualquer como entrada
# tendo como saída o seu dobre, triplo e raiz quadrada

# O programa aproxima em até 4 casas decimais

numero = float(input("Digite um número: "))

dobro = 2 * numero
triplo = 3 * numero
raiz = numero ** (1/2)
# Essas multiplicações poderiam ser feitas dentro do print

print("Número digitado: {:.4f}\n"
      "O seu DOBRO: {:.4f}\n"
      "O seu TRIPLO: {:.4f}\n"
      "A sua RAIZ QUADRADA: {:.4f}\n".format(numero, dobro, triplo, raiz))
