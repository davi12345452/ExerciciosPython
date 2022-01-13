# Programa recebe uma velocidade como entrada, devolvendo como
# saída se o motoristo estava dentro do limite, sendo que, caso
# tenha ultrapassado a velocidade, ele conta a multa

velocidade = int(input("Qual é a velocidade atual do carro em km: "))

if velocidade > 80:
    print("\nMULTADO! Você excedeu o limite permitido que é de 80Km/h\n"
          "Você deve pagar uma multa de R$280.00!")

print("Tenha um bom dia, dirija com segurança!")