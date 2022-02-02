# Programa que recebe como entrada notas e uma situação, devolvendo como
# saída um dicionário que analisa essas mesmas


def notas(*nota, sit):
    lista_notas = list()
    for elem in nota:
        lista_notas.append(elem)
    lista_notas.sort()
    dici_nota = dict()
    dici_nota["total"] = len(lista_notas)
    dici_nota["maior"] = lista_notas[-1]
    dici_nota["menor"] = lista_notas[0]
    dici_nota["media"] = sum(lista_notas)/len(lista_notas)
    if sit is True:
        if dici_nota["media"] >= 6.00:
            dici_nota["situação"] = "BOA"
        else:
            dici_nota["situação"] = "RUIM"
    print(dici_nota)

# Testando a função


notas(0, 2, 10, 9, sit=True)
notas(4, 6, 5, sit=True)
notas(6, 10, sit=True)



