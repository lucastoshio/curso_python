# Autor: Lucas Toshio
# Data 07/06/23


def cadastrar_usuario():
    with open("usuarios.txt", "a") as f:
        while True:
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
            f.write(f"Usuário: {username}\nSenha: {password}\n")
            print("Usuário cadastrado com sucesso!")
            resposta = input("Deseja cadastrar mais usuários? (s/n) ")
            if resposta.lower() != "s":
                break


def login():
    with open("usuarios.txt", "r") as f:
        data = f.read()
    while True:
        username = input("Digite seu nome de usuário: ")
        password = input("Digite sua senha: ")
        if f"Usuário: {username}\nSenha: {password}" in data:
            print("Login bem-sucedido!")
            break
        else:
            print("Usuário ou senha inválidos.")


def sum_two_numbers():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    print(f"A soma de {num1} e {num2} é {num1 + num2}.")


cadastrar_usuario()
login()
sum_two_numbers()
cadastrar_usuario()
