# Esse programa recebe um valor em real como entrada, devolvendo
# como saída a sua conversão em euro e dolar, levando em conta
# as cotações da manhã do dia 12/01/2022

valor = float(input("Qual o valor que você possui em dinheiro no momento? R$"))

dolar = valor / 5.58
euro = valor / 6.35

# Usei as cotações acima como base para a conversão

print("Levando como base as seguintes cotações:\n1 EUR = 6.35 BRL\n1 DOL = 5.58 BRL")
print("O usuário poderia converter o seus R${:.2f} em {:.2f} euros, ou em {:.2f} dólares".format(valor, euro, dolar))