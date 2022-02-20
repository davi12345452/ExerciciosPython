# Manipulando o arquivo, como abrir e cadastrar nele

from menu import *

def arquivo_existe(nome):
    try:
        arq = open(nome, 'rt')
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print("Houve um erro ao criar seu arquivo")
    else:
        print(f"Arquivo {nome} criado com sucesso")


def ler_arquivo(nome):
    try:
        arq = open(nome, "rt")
    except:
        print("Erro ao ler o arquivo")
    else:
        cabecalho("PESSOAS CADASTRADAS")
        for elem in arq:
            dado = elem.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
    finally:
        arq.close()


def cadastro(arquivo, nome="", idade=0):
    try:
        arq = open(arquivo, "at")
    except:
        print("Houve um ERRO ao abrir o arquivo")
    else:
        try:
            arq.write(f"{nome};{idade}\n")
        except:
            print("Houve um ERRO ao cadastrar a pessoa")
        else:
            print(f"Novo registro de {nome} adicionado.")
            arq.close()