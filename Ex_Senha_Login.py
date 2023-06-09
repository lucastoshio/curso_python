def login():
    username = input("Digite seu nome de usuário: ")
    password = input("Digite sua senha: ")
    while len(password) < 9 or not any(char.isdigit() for char in password) or not any(char.isupper() for char in password):
        print("Senha inválida. A senha deve ter pelo menos 9 caracteres, conter pelo menos uma letra maiúscula e pelo menos um número.")
        password = input("Digite sua senha novamente: ")
    with open("login.txt", "w") as f:
        f.write(f"Usuário: {username}\nSenha: {password}")
    print("Login bem-sucedido!")
    
def confirm_login():
    with open("login.txt", "r") as f:
        data = f.read()
    while True:
        username = input("Digite seu nome de usuário: ")
        password = input("Digite sua senha: ")
        if f"Usuário: {username}\nSenha: {password}" == data:
            print("Login bem-sucedido!")
            break
        else:
            print("Usuário ou senha inválidos.")
    
def sum_two_numbers():
    confirm_login()
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    print(f"A soma de {num1} e {num2} é {num1 + num2}.")

login()
sum_two_numbers()
login()