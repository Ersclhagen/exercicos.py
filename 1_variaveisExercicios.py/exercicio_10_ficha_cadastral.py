# Exercicio 10 - Ficha Cadastral Simulada
#
# Crie variáveis para:
# - nome
# - idade
# - altura
# - peso
# - cidade
#
# Em seguida, use o método `.format()` para exibir uma ficha formatada, como:
#
# ==== FICHA CADASTRAL ====
# Nome: João da Silva
# Idade: 32 anos
# Altura: 1.75 m
# Peso: 70 kg
# Cidade: São Paulo

nome = "João da Silva"
idade = 32
altura = 1.75
peso = 70
cidade = "São Paulo"


print("=== FICHA CADASTRAL ===")
mensagem = "\n{} tem \n{} anos, mede \n{:.2f} e pesa \n{}Kg, mora na cidade de \n{}.".format(
        nome, idade, altura, peso, cidade
)
print(mensagem)