# Autor: Lucas Toshio
# Data 06/06/23

Altura = float(input(" Digite sua altura ! "))
Sexo = input(" Informe seu Sexo ")

# Função upper() transforma a string em LETRAS MAIUSCULAS

if Sexo.upper() == "MASCULINO":
    nova_altura = float((72.7 * Altura) - 58)
    print(" Seu peso ideal é : ", nova_altura)

elif Sexo == "Feminino":
    nova_altura2 = float((62.1 * Altura) - 44.7)
    print(" Seu peso ideal é : ", nova_altura2)

else:
    print(" informações erradas  ERRO !! ")
