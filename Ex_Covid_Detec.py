print(" diagnostico Covid ")
Num_Pacientes = int(input(" quantros pacientes existem ? "))
infectados = 0

for x in range(Num_Pacientes):
    Tosse = input(" O Paciente {} esta tendo tosse. Sim ou Nao ? ".format(x + 1))
    febre = input(" O paciente {} esta tendo FEBRE. Sim ou Nao ? ".format(x + 1))
    respira = input( " O paciente {} esta tendo dificuldade de respirar. Sim ou Nao ? ".format(x + 1) )

    if Tosse == "sim" and febre == "sim" and respira == "sim":
        infectados += 1

print(" Quantidade de infectados é {}".format(infectados))
