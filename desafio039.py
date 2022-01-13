# Programa recebe como entrada um ano de nascimento, devolvendo como
# saída o ano de alistamento militar

from datetime import date

ano = int(input("Ano de nascimento: "))
ano_atual = date.today().year

if ano_atual - ano == 18:
    idade = ano_atual - ano
    print("\nQuem nasceu em {} tem {} anos em {}\n"
          "Você deve se alistar IMEDIATAMENTE!".format(ano, idade, ano_atual))

elif ano_atual - ano < 18:
    idade = ano_atual - ano
    print("\nQuem nasceu em {} tem {} anos em {}".format(ano, idade, ano_atual))
    tempo_restante = 18 - idade
    print("Ainda faltam {} para o seu alistamento.\n"
          "Você deve se alistar em {}".format(tempo_restante, (tempo_restante + ano_atual)))

else:
    idade = ano_atual - ano
    print("\nQuem nasceu em {} tem {} anos em {}".format(ano, idade, ano_atual))
    tempo_passado = idade - 18
    print("Você deveria ter se alistado a {} anos.\n"
          "Seu alistamento foi em {}".format(tempo_passado, (ano_atual - tempo_passado)))