# Autor: Lucas Toshio
# Data 07/06/23.

def cadastrar_usuario(username, password):
    with open("usuarios.txt", "a") as f:
        if (
            len(password) < 9
            or not any(char.isdigit() for char in password)
            or not any(char.isupper() for char in password)
            or not any(char.islower() for char in password)
        ):
            print(
                "Senha inválida. A senha deve ter pelo menos 9 caracteres, conter pelo menos uma letra maiúscula, pelo menos uma letra minúscula e pelo menos um número."
            )
        else:
            user = [username, password]
            f.write(f"{user}\n")
            print("Usuário cadastrado com sucesso!")


def deletar_usuario():
    with open("usuarios.txt", "r") as f:
        data = f.readlines()
    with open("usuarios.txt", "w") as f:
        for line in data:
            if "Usuário" not in line:
                f.write(line)
    print("Usuário deletado com sucesso!")


def editar_usuario():
    with open("usuarios.txt", "r") as f:
        data = f.readlines()
    with open("usuarios.txt", "w") as f:
        for line in data:
            if "Usuário" not in line:
                f.write(line)
    username = input("Digite o nome de usuário que deseja editar: ")
    password = input("Digite a nova senha: ")
    while (
        len(password) < 9
        or not any(char.isdigit() for char in password)
        or not any(char.isupper() for char in password)
    ):
        print(
            "Senha inválida. A senha deve ter pelo menos 9 caracteres, conter pelo menos uma letra maiúscula e pelo menos um número."
        )
        password = input("Digite a nova senha novamente: ")
    with open("usuarios.txt", "a") as f:
        user = [username, password]
        f.write(f"{user}\n")
    print("Usuário editado com sucesso!")


def visualizar_usuarios():
    with open("usuarios.txt", "r") as f:
        data = f.read()
    print(data)


def deletar_usuario_especifico():
    with open("usuarios.txt", "r") as f:
        data = f.readlines()
    with open("usuarios.txt", "w") as f:
        for line in data:
            if "Usuário" not in line:
                f.write(line)
    username = input("Digite o nome de usuário que deseja deletar: ")
    with open("usuarios.txt", "a") as f:
        for line in data:
            if username not in line:
                f.write(line)
    print(f"Usuário {username} deletado com sucesso!")


while True:
    print("\nMenu:")
    print("1 - Cadastrar usuário")
    print("2 - Deletar usuário")
    print("3 - Editar usuário")
    print("4 - Visualizar usuários")
    print("5 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        username = input("Digite seu nome de usuário: ")
        password = input("Digite sua senha: ")
        while (
            len(password) < 9
            or not any(char.isdigit() for char in password)
            or not any(char.isupper() for char in password)
        ):
            print(
                "Senha inválida. A senha deve ter pelo menos 9 caracteres, conter pelo menos uma letra maiúscula e pelo menos um número."
            )
            password = input("Digite sua senha novamente: ")
        cadastrar_usuario(username, password)

    elif opcao == "2":
        sub_opcao = input(
            "\nEscolha uma opção:\n1 - Deletar todos os usuários\n2 - Deletar um usuário específico\n"
        )
        if sub_opcao == "1":
            deletar_usuario()
        elif sub_opcao == "2":
            deletar_usuario_especifico()

    elif opcao == "3":
        editar_usuario()

    elif opcao == "4":
        visualizar_usuarios()

    elif opcao == "5":
        break

    else:
        print("\nOpção inválida. Tente novamente.")
