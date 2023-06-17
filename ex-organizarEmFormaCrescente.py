# Autor: Lucas Toshio
# Data 05/06/23


numeros = []

for i in range(5):
    numero = float(input("Digite um número: "))
    numeros.append(numero)

numeros.sort()

print("Os números em ordem crescente são:")
for numero in numeros:
    print(numero)
