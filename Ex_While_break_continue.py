# Autor: Lucas Toshio
# Data 07/06/23
#  Neste exemplo, o programa irá imprimir se o número
#  é par ou ímpar. Quando o número atinge 5, ele é
#  ignorado e o loop continua. Quando o número atinge 8,
#  o loop é interrompido.

numero = 0
while numero < 10:
    numero += 1
    if numero == 5:
        continue
    if numero == 8:
        break
    if numero % 2 == 0:
        print(f"O número {numero} é par")
    else:
        print(f"O número {numero} é ímpar")
