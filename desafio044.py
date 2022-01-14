# Programa que recebe de entrada o valor de um compra e devolve
# como saída o novo valor de acordo com a forma de pagamento

print("="*10 + " LOJA REAL " + "="*10)
valor = float(input("Valor da compra feita: R$"))

print("FORMAS DE PAGAMENTO\n"
      "[1] - à vista dinheiro/cheque\n"
      "[2] - à vista cartão\n"
      "[3] - 2x no cartão\n"
      "[4] - 3x ou mais no cartão\n")

escolha = int(input("A sua escolha: "))

if escolha == 1:
    valor_n = valor * 0.9
    print("Sua compra de R${} custará R${}".format(valor, valor_n))
elif escolha == 2:
    valor_n = valor * 0.95
    print("Sua compra de R${} custará R${}".format(valor, valor_n))
elif escolha == 3:
    print("Sua compra de R${} parcelada em até 2x continuará o mesmo valor".format(valor))
elif escolha == 4:
    valor_n = valor * 1.2
    parcela = int(input("Quantas parcelas: "))
    print("Você optou por pagar a sua compra de R${} em {}x no cartão\n"
          "O novo valor da compra será R${} ".format(valor, parcela, valor_n))
else:
    print("Você digitou uma opção inválida de pagamento.")

