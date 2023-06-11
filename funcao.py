def soma(a, b):
    """
    Função que recebe dois números e retorna a soma entre eles.
    """
    return a + b


def subtracao(a, b):
    """
    Função que recebe dois números e retorna a subtração entre eles.
    """
    return a - b


def multiplicacao(a, b):
    """
    Função que recebe dois números e retorna a multiplicação entre eles.
    """
    return a * b


def divisao(a, b):
    """
    Função que recebe dois números e retorna a divisão entre eles.
    """
    if b == 0:
        return "Não é possível dividir por zero."
    else:
        return a / b


print(soma(2, 3))
print(subtracao(5, 2))
print(multiplicacao(3, 4))
print(divisao(10, 2))
