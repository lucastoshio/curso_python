nomes = []
nomes = [input(print("informe o nome do aluno"))]

while True:
    acumulador = input(
        print(" voce quer cadastrar o nome de mais algum aluno ? SIM OU NAO ?")
    )
    if acumulador == "sim":
        nome = input(print("informe os nomes dos alunos"))
        nomes.append(nome)
    else:
        break

print(nomes)
