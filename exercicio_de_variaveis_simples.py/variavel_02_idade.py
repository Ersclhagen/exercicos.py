# Exercício 02 - Variável numérica
# Peça para o usuário digitar sua idade e imprima quantos anos ele terá daqui a 10 anos.

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
idade_futura = idade + 10

print(f"Olá, {nome.title()}, daqui há 10 anos você terá {idade_futura} anos!")