# Exercício 01 - Nome completo com input e f-string
# Peça para o usuário digitar nome e sobrenome e mostre o nome completo formatado.

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
print(f"Nome completo: {nome.title()} {sobrenome.title()}")
