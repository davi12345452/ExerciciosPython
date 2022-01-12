# Programa em que o usuário da como entrada um ângulo, recebendo
# como saída o seno, cosseno e tangente deste ângulo

import math

angulo = float(input("Digite o ângulo que você deseja: "))

sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print("SENO de {} = {:.2f}".format(angulo, sen))
print("COSSENO de {} = {:.2f}".format(angulo, cos))
print("TANGENTE de {} = {:.2f}".format(angulo, tan))