# Autor: Lucas Toshio
# Data 07/06/23

def verifica_nome(nome):
    if len(nome) > 4:
        print("O nome tem mais de 4 letras!")
    else:
        print("O nome tem 4 letras ou menos.")


nome = input("Digite um nome: ")
verifica_nome(nome)
