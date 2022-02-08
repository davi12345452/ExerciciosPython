# Programa que recebe um nome de site e verifica se ele está ou não conectado(ou seja, se ele existe)
# caso o usuário esteja desconectado da internet, o programa devolverá que o site não está conectado

import urllib
import urllib.request

site = str(input("Digite o URL do site que deseja verificar: "))

try:
    urllib.request.urlopen(site)
except urllib.error.URLError:
    print("NÃO CONECTADO")
else:
    print("CONECTADO")