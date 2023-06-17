# Autor: Lucas Toshio
# Data 07/06/23
# Criando um dicionario chamado Contato
contato = {"@camila": "camila", "@amanda": "amanda", "@fernanda": "fernanda"}

# função keys() retorta a chave
for insta in contato.keys():
    print(insta)
# função values() retorna o valor
for atriz in contato.values():
    print(atriz)
# função items() retorna ambos
for insta, atriz in contato.items():
    print(" o instagran de {} é {}".format(atriz, insta))
