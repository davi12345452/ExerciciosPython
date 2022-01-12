# Programa que recebe como entrada uma string do usuário
# tendo como saída uma mensagem ou música

from playsound import playsound

resposta = str(input("Você deseja escutar uma música?[S]/[N] ")).upper()

# Usuário coloca dentro dos parenteses do playsound o arquivo mp3 da música

if resposta == "S":
    playsound()
else:
    print("Que pena, você está perdendo ein...")