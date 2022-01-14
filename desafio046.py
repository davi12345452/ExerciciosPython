# Programa de contagem regressiva, não tem entrada
# só a saída

from time import sleep

for cont in range(10, 0, -1):
    print(cont)
    sleep(1)

print("ACABOU!!")