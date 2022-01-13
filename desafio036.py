# Programa recebe como entrada o valor da casa, o tempo de financiamento
# e o salário do cliente, devolvendo como saída se o empréstimo será ou
# não concedido. Programa leva em conta um juros de 10% ano e que a pres-
# tação não pode exceder 30% do salário

print("\nSeja bem vindo, a taxa anual do financiamento é de 5%\n")

valor = float(input("Valor do imóvel: R$"))
tempo = float(input("Tempo para quitar o financiamento em anos: "))
salario = float(input("O seu salário mensal: R$"))

financiamento = valor*(1.05**tempo)
parcela = financiamento / (12*tempo)

if parcela > (0.3 * salario):
    print("Empréstimo NÃO CONCEDIDO")
else:
    print("Empréstimo CONCEDIDO, sua parcela mensal será de R${:.2f}".format(parcela))