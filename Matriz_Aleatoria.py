import random

while True:
    lin = int(input("digite o numero de linhas"))
    colunas = int(input("digite o numero de colunas "))

    if lin > 0 and colunas > 0:
        M = []
        for i in range(lin):
            Linha = []
            for j in range(colunas):
                num = random.randint(
                    0, 11
                )  # comando randon.randint gera um numero inteiro aleatoriamente
                Linha.append(num)
            M.append(Linha)
        break
print(M)

# Printar em forma de matriz
for i in range(lin):
    for j in range(colunas):
        print(M[i][j], end=" ")
    print("")

# Printa o elemento especificado, nesse caso linha 0 coluna 0
print(M[0][0])
