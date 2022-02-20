# Programa principal, onde as funções criadas como módulo são usadas

from arquiv import *
from menu import *


lista_principal = ["Ver pessoas cadastradas", "Cadastrar nova Pessoa", "Sair do Sistema"]
arquivo = 'desafio115.txt'

if not arquivo_existe(arquivo):
    criar_arquivo(arquivo)


while True:
    resp = layout(lista_principal)
    if resp == 1:
        ler_arquivo(arquivo)
    elif resp == 2:
        cabecalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = int(input("Idade: "))
        cadastro(arquivo, nome, idade)
    elif resp == 3:
        cabecalho("Saindo do sitema")
        break
    else:
        print('\033[31mERRO: Digite uma opção válida!\033[m')
