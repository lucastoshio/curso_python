# Autor: Lucas Toshio
# Data 06/06/23

salario_Atual = float(input("Digite o salario atual"))
Cargo_Atual = input("Digite o cargo atual")

if Cargo_Atual == "Programador":
    print(" Cargo valido")
    print("Seu novo salario é: ", salario_Atual * 1.5)

elif Cargo_Atual == "Analista de sistema":
    print(" Cargo valido")
    print("Seu novo salario é: ", salario_Atual * 1.4)

elif Cargo_Atual == "Analista de banco de dados":
    print(" Cargo valido")
    print("Seu novo salario é: ", salario_Atual * 1.3)

else:
    print("cargo invalido")
