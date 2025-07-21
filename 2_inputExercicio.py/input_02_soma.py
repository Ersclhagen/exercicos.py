# Exercício 02 - Soma de dois números
#
# Peça para o usuário digitar dois números inteiros.
# Some esses números e exiba o resultado na tela com uma frase,
# no formato: "A soma de X e Y é igual a Z."

numero1 = int(input("Digite um número inteiro:"))
numero2 = int(input("Digite um número inteiro:"))


soma = numero1 + numero2

print("A soma de {} e {} é igual a {}.".format(numero1, numero2, soma))

