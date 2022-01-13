# Porgrama recebe como entrada um nome completo, devolvendo como
# saída algumas alterações e constatações acerca da string

from time import sleep

nome = str(input("Digite o seu nome completo: "))

print("Analisando...")
sleep(1.5)

print("Seu nome só com letras maiúsculas ficaria: %s" % (nome.upper()))
# Comando upper coloca todas letras em maiúsculas
print("Seu nome só com letras minúsculas ficaria: %s" % (nome.lower()))
# Comando lower coloca todas letras em minúsculas
print("Seu nome possui %d letras" % (len(nome) - nome.count(" ")))
# Comando len() conta os caracteres da string, enquanto o count somente conta
# os espaços em branco, permitindo ter precisão no número de letras do nome
primeiro_n = nome.split()
print("Seu primeiro nome é %s e tem %d letras" % (primeiro_n[0], len(primeiro_n[0])))
# Comando split "corta" a string onde tem espaço, formando uma lista, por exemplo
# Joao da Silva, ficaria ["Joao", "da", "Silva"]. Logo, após criada a lista, vamos
# manipular seu elemento 0 e assim teremos o nome e poderemos usar o len nele.

