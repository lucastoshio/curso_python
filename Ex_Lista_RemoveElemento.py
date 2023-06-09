Alunos = []
Alunos.append("leticia")
Alunos.append("maria")
Alunos.append("lucas")
Alunos.append("maria")
Alunos.append("lucas")
Alunos.append("lucas")
Alunos.insert(6, "maria")

print(Alunos)

Alunos.pop(0)  # remove o 1 iten da lista
print(Alunos)

Alunos.remove("lucas")  # remove um elemento "especificar"
print(Alunos)

for nome in Alunos:
    if nome == "maria":
        Alunos.remove("maria")
        print(Alunos)
      

print(Alunos)

Alunos.clear()  # apaga tudo
print(Alunos)
